from datetime import datetime
from mongoengine import Document, DateTimeField, IntField


class BaseDocument(Document):
    """Base Document with common fields across the other models."""

    creation_time = DateTimeField(required=True, default=datetime.now)
    last_update_time = DateTimeField(required=True, default=datetime.now)
    deletion_time = DateTimeField()

    # NOTE: This extra field is used only for the migration of the database, its not needed
    # after the migration an can be safely removed afterwards, its needed to pass the correct references
    # to the new instance
    # WARNING: if this models are used in another project delete this field
    public_id = IntField(required=True)

    meta = {"abstract": True}

    def save(
        self,
        force_insert=False,
        validate=True,
        clean=True,
        write_concern=None,
        cascade=None,
        cascade_kwargs=None,
        _refs=None,
        save_condition=None,
        signal_kwargs=None,
        **kwargs,
    ):
        self.last_update_time = datetime.now()
        super().save(
            force_insert,
            validate,
            clean,
            write_concern,
            cascade,
            cascade_kwargs,
            _refs,
            save_condition,
            signal_kwargs,
            **kwargs,
        )

    def delete(
        self,
        force_insert=False,
        validate=True,
        clean=True,
        write_concern=None,
        cascade=None,
        cascade_kwargs=None,
        _refs=None,
        save_condition=None,
        signal_kwargs=None,
        **kwargs,
    ):
        self.deletion_time = datetime.now()
        super().save(
            force_insert,
            validate,
            clean,
            write_concern,
            cascade,
            cascade_kwargs,
            _refs,
            save_condition,
            signal_kwargs,
            **kwargs,
        )
