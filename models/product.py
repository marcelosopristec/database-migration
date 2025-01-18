from mongoengine import (
    StringField,
    IntField,
    ReferenceField,
    CASCADE,
)
from models.base_document import BaseDocument
from models.customer import CustomerDocument


class ProductDocument(BaseDocument):
    """Model to represent the product document structure."""
    product_id = IntField(required=True)
    product_name = StringField(required=True)
    description = StringField(required=True)
    customer = ReferenceField(CustomerDocument, reverse_delete_rule=CASCADE)

    meta = {
        "collection": "products",
    }
