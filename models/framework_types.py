import mongoengine as me
from datetime import datetime


class RenderMetaSection(me.EmbeddedDocument):
    type = me.StringField(required=True)
    name = me.StringField(required=True)
    label = me.StringField(required=True)
    fields = me.ListField(me.StringField(), required=True)


class RenderMetaSummary(me.EmbeddedDocument):
    fields = me.ListField(me.StringField(), required=True)


class RenderMeta(me.EmbeddedDocument):
    icon = me.StringField()
    sections = me.ListField(me.EmbeddedDocumentField(RenderMetaSection))
    externals = me.ListField(me.DictField())
    summary = me.EmbeddedDocumentField(RenderMetaSummary)


class Field(me.EmbeddedDocument):
    type = me.StringField(required=True)
    name = me.StringField(required=True)
    label = me.StringField(required=True)
    required = me.BooleanField(default=False)
    regex = me.StringField()
    default = me.StringField()
    options = me.ListField(me.DictField())
    value = me.DynamicField()
    ref_types = me.ListField(me.IntField())
    summaries = me.ListField(me.DictField())


class ACLGroups(me.EmbeddedDocument):
    includes = me.DictField()


class ACL(me.EmbeddedDocument):
    activated = me.BooleanField(default=False)
    groups = me.EmbeddedDocumentField(ACLGroups)


class FrameworkTypesDocument(me.Document):
    public_id = me.IntField(required=True, unique=True)
    name = me.StringField(required=True)
    selectable_as_parent = me.BooleanField(default=False)
    global_template_ids = me.ListField(me.StringField())
    active = me.BooleanField(default=True)
    author_id = me.IntField()
    editor_id = me.IntField()
    label = me.StringField(required=True)
    version = me.StringField()
    description = me.StringField()
    render_meta = me.EmbeddedDocumentField(RenderMeta)
    fields = me.ListField(me.EmbeddedDocumentField(Field))
    acl = me.EmbeddedDocumentField(ACL)
    creation_time = me.DateTimeField(default=datetime.utcnow)
    last_edit_time = me.DateTimeField(default=datetime.utcnow)

    meta = {
        'collection': 'framework.types',
    }
