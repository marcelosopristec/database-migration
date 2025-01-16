from mongoengine import StringField, ReferenceField, IntField, CASCADE

from models.base_document import BaseDocument


class NodesByTestDocument(BaseDocument):
    """Model to collection nodes_by_test."""

    node_reference = IntField(min_value=0, required=True)
    test = ReferenceField(TestDocument, required=True, reverse_delete_rule=CASCADE)
    node_type = StringField(required=True)
    vendor = ReferenceField(VendorDocument, required=True, reverse_delete_rule=CASCADE)
    country = ReferenceField(
        CountryDocument, required=True, reverse_delete_rule=CASCADE
    )

    meta = {
        "collection": "nodes_by_test",
    }
