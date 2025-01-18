from typing import List
from models.dynamic_document import GenericDocument
from models.framework_types import FrameworkTypesDocument, Field
from models.framework_objects import FrameworkObjectsDocument, ObjectField
from models.customer import CustomerDocument
from models.customer_networkcode import CustomerNetworkcodeDocument
from models.product import ProductDocument
from models.nodes_x_vendor import NodesXVendorDocument
from models.test_type import TestTypeDocument
from models.test import TestDocument
from models.vendors import VendorDocument
from models.countries import CountryDocument
from models.nodes_by_test import NodesByTestDocument
from models.towers_by_test import TowersByTestDocument
from models.nodes_x_products import NodesXProductsDocument


# TODO: How to get correct type -> document map without hardcoding it
type_map = {
    4: CustomerDocument,
    9: CustomerNetworkcodeDocument,
    16: ProductDocument,
    17: TestTypeDocument,
    18: TestDocument,
    19: TowersByTestDocument,
    20: VendorDocument,
    21: CountryDocument,
    22: NodesByTestDocument,
    23: NodesXVendorDocument,
    24: NodesXProductsDocument
}


def safe_int(value, default=0):
    if value is None:
        return default
    try:
        return int(value)
    except ValueError:
        return default


class MigrationAssetManagerSchemas:
    framework_types: dict[int, FrameworkTypesDocument] = {}
    documents_collections = []

    def build_document(self, fields: List[Field]) -> dict:
        value = {}

        for field in fields:
            value[field.name] = field.value

        return value

    def save_framework_type(self):
        """
        This method obtain all the schema types from frameworks.type, this information is related to the table type or collection that we need to complete the migration process
        The values will be saved in the local attr "framework_types" to avoid unnecessary request.
        """

        print("Getting all frameworks.type documents ...")

        documents = FrameworkTypesDocument.objects(
            public_id__in=[4, 9, 16, 17, 18, 19, 20, 21, 22, 23, 24]
        ).only("name", "fields", "public_id")

        for doc in documents:
            self.framework_types[doc.public_id] = doc

        print(f"Total frameworks.type documents registered: {len(documents)}")

    def generate_documents(self):
        """
        Migrates documents from FrameworkObjectsDocument to pre-definec document
        based on their type_id and the framework_types mapping.
        """

        print("Getting all frameworks.objects documents to migrate ...")

        # TODO: generate correct insert order based on each framework type references
        insert_order = [4, 9, 17, 20, 21, 16, 18, 19, 22, 23, 24]

        # TODO: double for loop is really needed?
        # TODO: maybe change for a normal for in over the insert_order list
        for i in range(len(insert_order)):
            framework_type = self.framework_types[insert_order[i]]
            print(f"Processing {framework_type.name}")
            collection = type_map.get(insert_order[i])
            if collection is None:
                print("ERROR: Document Model not founded")
                return

            for framework_object in FrameworkObjectsDocument.objects(type_id=insert_order[i]).no_cache():
                object_dict = self._process_fields_list(field_list=framework_type.fields,
                                                        object_fields=framework_object.fields,
                                                        public_id=framework_object.public_id)
                new_document = collection(**object_dict)
                new_document.save()

    def _process_fields_list(self, field_list: list[Field], object_fields: list[ObjectField], public_id: int) -> dict:
        """
        Transforms the given field list and fields values to a python dict

        NOTE: This functions asumes that if a ref field is founded the reference was already inserted before, so
        it will try to find the reference id, otherwise if the reference is not founded it will be set to None,
        this makes it posible that if you try to create a document from the returned dict the validation will failed
        if the reference field is required
        """
        object_dict = {}

        object_dict["public_id"] = public_id

        for field in field_list:
            value = next((object_field.value for object_field in object_fields
                          if object_field.name == field.name), None)
            match field.type:
                case "text":
                    if field.regex is not None:
                        object_dict[field.name] = safe_int(value)
                    else:
                        object_dict[field.name] = value

                case "ref":
                    # NOTE: if the referency type is not founded on the map, reference is set to None
                    collection = type_map.get(field.ref_types[0])

                    if collection is None:
                        object_dict[field.name] = None
                    else:
                        try:
                            reference_object = collection.objects.get(public_id=value)
                            object_dict[field.name] = reference_object
                        except Exception:
                            print(f"Error obtaining reference with public_id {value}")
                            object_dict[field.name] = None

                case "checkbox":
                    object_dict[field.name] = value

                # TODO: define what to do with the default case
                case _:
                    pass

        return object_dict

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
            except Exception:
                errors += 1

        print(f"Process complete, success: {success} errors: {errors}")
