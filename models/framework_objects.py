from mongoengine import (
    Document,
    EmbeddedDocument,
    EmbeddedDocumentListField,
    StringField,
    BooleanField,
    IntField,
    DateTimeField,
    ListField
)

class Field(EmbeddedDocument):
    """Model to represent individual field data."""
    name = StringField(required=True)
    value = StringField()

class FrameworkObjectsDocument(Document):
    """Model to represent the document structure."""
    type_id = IntField(required=True)
    status = BooleanField(required=True)
    version = StringField(required=True)
    creation_time = DateTimeField(required=True)
    author_id = IntField(required=True)
    last_edit_time = DateTimeField(required=True)
    editor_id = IntField(required=True)
    active = BooleanField(required=True)
    fields = EmbeddedDocumentListField(Field, required=True)
    multi_data_sections = ListField(default=[])
    public_id = IntField(required=True)
    views = IntField(default=0)

    meta = {
        "collection": "framework.objects",
        "strict": False,
    }
