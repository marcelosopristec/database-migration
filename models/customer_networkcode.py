from mongoengine import StringField, ReferenceField

from models.base_document import BaseDocument
from .customer import CustomerDocument

class CustomerNetworkcodeDocument(BaseDocument):
    """Model to represent the customer_networkcode document structure."""

    customer = ReferenceField(CustomerDocument, required=True, reverse_delete_rule=2)
    networkcode = StringField(required=True)

    meta = {
        "collection": "customer_networkcode",
    }
