from mongoengine import StringField, ReferenceField, IntField, CASCADE

from models.base_document import BaseDocument
from models.test import TestDocument
from models.countries import CountryDocument
from models.vendors import VendorDocument


class NodesByTestDocument(BaseDocument):
    """Model to collection nodes_by_test."""

    node_reference = IntField(min_value=0, required=True)
    test = ReferenceField(TestDocument, reverse_delete_rule=CASCADE)
    node_type = StringField(required=True)
    vendor = ReferenceField(VendorDocument, reverse_delete_rule=CASCADE)
    country = ReferenceField(
        CountryDocument, reverse_delete_rule=CASCADE
    )

    meta = {
        "collection": "nodes_by_test",
    }
