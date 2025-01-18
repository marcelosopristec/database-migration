from mongoengine import (
    StringField,
    ReferenceField,
    CASCADE
)
from models.base_document import BaseDocument
from models.test import TestDocument


class TowersByTestDocument(BaseDocument):
    """Model to represent the towers by test document structure."""
    tower_name = StringField(required=True)
    test = ReferenceField(TestDocument, reverse_delete_rule=CASCADE)

    meta = {
        "collection": "towers_by_test",
    }
