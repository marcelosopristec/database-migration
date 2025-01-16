from mongoengine import StringField, ReferenceField, IntField, CASCADE

from models.base_document import BaseDocument


class NodesXVendorDocument(BaseDocument):
    """Model to collection nodes_x_vendor."""

    vendor = ReferenceField(VendorDocument, required=True, reverse_delete_rule=CASCADE)
    country = ReferenceField(
        CountryDocument, required=True, reverse_delete_rule=CASCADE
    )
    node = IntField(min_value=0, required=True)
    node_type = StringField(required=True)
    node_name = StringField(required=True)

    meta = {
        "collection": "nodes_x_vendor",
    }
