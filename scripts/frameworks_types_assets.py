import json
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
        
        documents = FrameworkTypesDocument.objects.only('name', 'fields').all()

        for doc in documents:

            self.framework_types[doc.public_id] = {
                "doc": doc,
                "cls": None
            }

        print(f"Total frameworks.type documents registered: {len(documents)}")


    def generate_documents(self):
        """
        Migrates documents from FrameworkObjectsDocument to dynamically determined collections 
        based on their type_id and the framework_types mapping.
        """

        print("Getting all frameworks.objects documents to migrate ...")
        
        documents = FrameworkObjectsDocument.objects(type_id=4)
        self.documents_collections = documents

        print(f"Total frameworks.objects documents found: {len(documents)}")
       

    def save_documents(self):
        success = 0
        errors = 0

        for doc in self.documents_collections:
            try:
                collection = self.framework_types[doc.type_id]

                class DynamicCollection(GenericDocument):
                    meta = {
                        "collection": collection.name,
                        "allow_inheritance": False,
                    }

                value_to_insert = self.build_document(doc.fields)
                document = DynamicCollection(**value_to_insert)
                document.save()

                success += 1
            except Exception as error:
                errors += 1


        print(f"Process complete, success: {success} errors: {errors}")