from datetime import datetime
from mongoengine import Document, DateTimeField


class BaseDocument(Document):
    """Model to collection vendors."""

    creation_time = DateTimeField(required=True, default=datetime.datetime.now)
    last_update_time = DateTimeField(required=True, default=datetime.datetime.now)
    deletion_time = DateTimeField()

    meta = {"allow_inheritance": True, "abstract": True}

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
        self.last_update_time = datetime.datetime.now()
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
        self.deletion_time = datetime.datetime.now()
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
