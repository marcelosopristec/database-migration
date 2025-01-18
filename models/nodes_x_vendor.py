from mongoengine import StringField, ReferenceField, IntField, CASCADE

from models.base_document import BaseDocument
from models.vendors import VendorDocument
from models.countries import CountryDocument


class NodesXVendorDocument(BaseDocument):
    """Model to collection nodes_x_vendor."""

    vendor = ReferenceField(VendorDocument, reverse_delete_rule=CASCADE)
    country = ReferenceField(
        CountryDocument, reverse_delete_rule=CASCADE
    )
    node = IntField(min_value=0, required=True)
    node_type = StringField(required=True)
    node_name = StringField(required=True)

    meta = {
        "collection": "nodes_x_vendor",
    }
