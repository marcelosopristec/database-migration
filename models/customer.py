from mongoengine import (
    StringField,
    BooleanField,
    IntField,
)
from models.base_document import BaseDocument


class CustomerDocument(BaseDocument):
    """Model to represent the customer document structure."""
    customer_id = IntField(required=True)
    division_id = IntField(required=True)
    short_name = StringField(required=True)
    description = StringField(required=True)
    company_name = StringField(required=True)
    alert_webhook_id = StringField(required=False)
    conexion_zenoss_ok = BooleanField(required=True, default=False)
    conexion_catchpoint_ok = BooleanField(required=True, default=False)
    scope = StringField(required=False)
    sector = StringField(required=False)
    subsector = StringField(required=False)

    meta = {
        "collection": "customers",
    }

