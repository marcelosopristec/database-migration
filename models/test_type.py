from mongoengine import (
    StringField,
    IntField,
)
from models.base_document import BaseDocument


class TestTypeDocument(BaseDocument):
    """Model to represent the test type document structure."""
    test_type_id = IntField(required=True)
    name = StringField(required=True)
    description = StringField(required=True)

    meta = {
        "collection": "test_types",
    }
