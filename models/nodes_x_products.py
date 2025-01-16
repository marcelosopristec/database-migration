from mongoengine import ReferenceField, CASCADE

from models.base_document import BaseDocument


class NodesXProductsDocument(BaseDocument):
    """Model to collection nodes_x_products."""

    product = ReferenceField(
        ProductDocument, required=True, reverse_delete_rule=CASCADE
    )
    node_x_vendor = ReferenceField(
        NodeXVendorDocument, required=True, reverse_delete_rule=CASCADE
    )

    meta = {
        "collection": "nodes_x_products",
    }
