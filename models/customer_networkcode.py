from mongoengine import (
    Document,
    StringField,
    ReferenceField,
)

from .customer import CustomerDocument

class CustomerNetworkcodeDocument(Document):
    """Model to represent the customer document structure."""
    customer = ReferenceField(CustomerDocument, required=True, reverse_delete_rule=2)
    networkcode = StringField(required=True)

    meta = {
        "collection": "customer_networkcode",
    }
