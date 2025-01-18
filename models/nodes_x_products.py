from mongoengine import ReferenceField, CASCADE

from models.base_document import BaseDocument
from models.nodes_x_vendor import NodesXVendorDocument
from models.product import ProductDocument


class NodesXProductsDocument(BaseDocument):
    """Model to collection nodes_x_products."""

    product = ReferenceField(
        ProductDocument, reverse_delete_rule=CASCADE
    )
    node_x_vendor = ReferenceField(
        NodesXVendorDocument, reverse_delete_rule=CASCADE
    )

    meta = {
        "collection": "nodes_x_products",
    }
