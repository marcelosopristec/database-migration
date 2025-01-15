from mongoengine import DynamicDocument

class GenericDocument(DynamicDocument):
    meta = {
        "abstract": True,
        "allow_inheritance": True,
    }
