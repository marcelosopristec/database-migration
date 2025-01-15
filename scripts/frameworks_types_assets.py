from typing import List
from models.dynamic_document import GenericDocument
from models.framework_types import FrameworkTypesDocument
from models.framework_objects import FrameworkObjectsDocument, Field


class MigrationAssetManagerSchemas:

    framework_types = {}
    documents_collections = []

    def build_document(self, fields: List[Field]) -> dict:
        value = {}

        for field in fields:
            value[field.name] = field.value

        return value
    
    def save_framework_type(self):
        """"
        This mehtod obtain all the schema types from frameworks.type, this information is related to the table type or collection that we need to complete the migration process
        The values will be saved in the local attr "framework_types" to avoid unnecessary request.
        """

        print("Getting all frameworks.type documents ...")
        total_registered = 0
        documents = FrameworkTypesDocument.objects.all()

        for doc in documents:
            total_registered += 1
            self.framework_types[doc.public_id] = doc

        print(f"Total frameworks.type documents registered: {len(self.framework_types)}")

    def generate_documents(self):
        """
        Migrates documents from FrameworkObjectsDocument to dynamically determined collections 
        based on their type_id and the framework_types mapping.
        """

        print("Getting all frameworks.objects documents to migrate ...")
        
        documents = FrameworkObjectsDocument.objects.all()
        self.documents_collections = documents

       

    def save_documents(self):
         for doc in self.documents_collections:
            collection = self.framework_types[doc.type_id]

            class DynamicCollection(GenericDocument):
                meta = {
                    "collection": collection.name,
                }

            value_to_insert = self.build_document(doc.fields)
            document = DynamicCollection(**value_to_insert)
            document.save()

            print(f"Document inserted successfully into '{collection.name}'")
