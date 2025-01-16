from mongoengine import (
    Document,
    StringField,
    BooleanField,
    IntField,
)


class CustomerDocument(Document):
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
