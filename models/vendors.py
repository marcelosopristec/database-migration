from mongoengine import StringField

from models.base_document import BaseDocument


class VendorDocument(BaseDocument):
    """Model to collection vendors."""

    vendor_name = StringField(required=True)
    vendor_short_name = StringField(required=True)
    description = StringField(required=True)

    meta = {
        "collection": "vendors",
    }
