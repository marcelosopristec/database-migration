from mongoengine import StringField, IntField

from models.base_document import BaseDocument


class CountriesDocument(BaseDocument):
    """Model to collection countries."""

    country_id = IntField(min_value=0, required=True)
    short_name = StringField(required=True)
    full_name = StringField(required=True)
    description = StringField(required=True)

    meta = {
        "collection": "countries",
    }
