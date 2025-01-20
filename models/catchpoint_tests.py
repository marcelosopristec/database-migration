from mongoengine import (
    StringField,
    IntField,
    ReferenceField
)

from models.base_document import BaseDocument

from .customer import CustomerDocument
from .test_type import TestTypeDocument


class CatchpointTestDocument(BaseDocument):
    """Model to represent the catchpoint_tests document structure."""

    division_id = IntField(required=True)
    test_catchpoint_id = IntField(required=True)

    status = StringField(required=True)
    test_name = StringField(required=True)
    created_by = StringField(required=False)
    cmdb_impact = StringField(required=False)
    cmdb_hostname = StringField(required=False)
    main_reference = StringField(required=True)
    cmdb_alert_name = StringField(required=False)
    cmdb_logical_name = StringField(required=False)
    configuration_node_type = StringField(required=False)

    product = IntField(required=True) # TODO create reference
    customer = ReferenceField(CustomerDocument, required=True, reverse_delete_rule=2)
    test_type = ReferenceField(TestTypeDocument, required=True, reverse_delete_rule=2)

    meta = {
        "collection": "catchpoint_tests",
    }
