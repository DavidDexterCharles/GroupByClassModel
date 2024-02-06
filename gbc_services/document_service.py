#pylint: disable=R0903:too-few-public-methods
#pylint: disable=C0114:missing-module-docstring
#pylint: disable=C0304:missing-final-newline
#pylint: disable=C0115:missing-class-docstring
#pylint: disable=C0303:trailing-whitespace

import re
import json
import uuid
from typing import List
from collections import Counter

class Document:
    def __init__(self,  title, content, categories:List,term_vector):
        self.id = str(uuid.uuid4())
        self.title = title
        self.content = content
        self.categories = categories
        self.term_vector:Counter = term_vector

# class Documents:
#     def __init__(self, documents:List[Document]):
#         self.documents = documents


class DocumentService:
        
    def json_to_doc(self,json_data):
        '''
        converts json structure below to list of documents with their 
        respective termvectors.
        Example:

        doc=

        [
            {
            "title": "Document 1",
            "content": "This is the content of Document 1.",
            "categories": ["Category A", "Category B"]
            },
           ....
        ]

        [Document(doc['title'], doc['content'], doc['categories'],_term_vector(doc))]
        '''
        try:
            data = json.loads(json_data)
            documents_data = data#data.get('documents', [])
            # Convert JSON data to a list of Document instances
            documents = [
                Document(doc['title'], doc['content'], doc['categories'],self._term_vector(doc))
                for doc in documents_data
            ]
            # Return a Documents instance
            return documents
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None
        
    def _term_vector(self,doc):
        tv=Counter(self._pre_process(doc['content']).split(" "))
        return tv
    def _pre_process(self,text):
        text = text.lower()
        # remove tags
        text = re.sub("</?.*?>", " <> ", text)  
        # remove special characters and digits
        text = re.sub("(\\d|\\W)+", " ", text)  
        return text