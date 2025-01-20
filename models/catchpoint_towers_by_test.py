from mongoengine import (
    StringField,
    ReferenceField
)

from models.base_document import BaseDocument

from .test_type import TestTypeDocument

class CatchpointTowersByTestDocument(BaseDocument):
    """Model to represent the catchpoint_towers_by_test document structure."""

    tower_name = StringField(required=True)
    test = ReferenceField(TestTypeDocument, required=True, reverse_delete_rule=2)

    meta = {
        "collection": "catchpoint_towers_by_test",
    }
