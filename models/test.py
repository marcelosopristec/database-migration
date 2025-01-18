from mongoengine import (
    StringField,
    IntField,
    ReferenceField,
    CASCADE,
)
from models.base_document import BaseDocument
from models.customer import CustomerDocument
from models.product import ProductDocument
from models.test_type import TestTypeDocument


class TestDocument(BaseDocument):
    """Model to represent the test document structure."""
    test_catchpoint_id = IntField(required=True)
    division_id = IntField(required=True)
    test_name = StringField(required=True)
    customer = ReferenceField(CustomerDocument, reverse_delete_rule=CASCADE)
    product = ReferenceField(ProductDocument, reverse_delete_rule=CASCADE)
    test_type = ReferenceField(TestTypeDocument, reverse_delete_rule=CASCADE)
    main_reference = StringField(required=True)
    configuration_node_type = StringField(required=False)
    created_by = StringField(required=False)

    # TODO: this field is used as a flag of the state of the test, check if is posible to change implementation to a BooleanField
    status = StringField(required=True)

    # TODO: check if cmdb values need to be required or not
    cmdb_logical_name = StringField()
    cmdb_alert_name = StringField()
    cmdb_hostname = StringField()
    cmdb_impact = StringField()

    meta = {
        "collection": "tests",
    }
