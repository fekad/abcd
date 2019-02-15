# from mongoengine import Document, EmbeddedDocument, fields
from app.db import db

from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    DateTimeField, EmbeddedDocumentField, EmbeddedDocumentListField,
    ListField, ReferenceField, StringField, IntField, BooleanField, FloatField, DictField, ObjectIdField
)


class Databases(Document):
    meta = {'collection': 'databases'}
    name = StringField(required=True)
    description = StringField(max_length=300)
    tags = ListField(StringField(max_length=30))


# class Arrays(EmbeddedDocument):
#     meta = {'strict': False}
#     numbers = ListField(IntField())
#     # positions = db.ListField(db.ListField(db.FloatField()))
#
#     # forces = db.ListField()

class Arrays(EmbeddedDocument):
    meta = {'strict': False}
    numbers = ListField(IntField())
    positions = ListField(ListField(FloatField()))


# forces = db.ListField()

# #
# class Info(EmbeddedDocument):
#     meta = {'strict': False}
#     #     pbc = ListField(BooleanField())
#     #     # cell = db.ListField(db.ListField(db.FloatField()), required=True)
#     #
#     #     energy = FloatField()
#     #
#     calculator_name = StringField()
#     calculator_parameters = ListField()


#     constraints = ListField()
#
#
# class Atoms(db.Document):
#     meta = {'collection': 'atoms', 'strict': False}
#
#     arrays = DictField(EmbeddedDocumentField(Arrays))
#     # info = db.EmbeddedDocumentField(Info)

class Derived(EmbeddedDocument):
    # meta = {'strict': False}

    elements = DictField(IntField())
    arrays_keys = ListField(StringField())
    info_keys = ListField(StringField())


class Atoms(Document):
    meta = {'collection': 'atoms', 'strict': False}
    # id = ObjectIdField()
    # pbc = ListField(db.BooleanField())
    # numbers = db.ListField(db.IntField())
    arrays = DictField()
    info = DictField()
    derived = EmbeddedDocumentField(Derived)
    arrays = EmbeddedDocumentField(Arrays)

    # positions = db.ListField(db.ListField(db.FloatField()))

    @classmethod
    def from_ase(cls, atoms):
        return cls()


sample = {
    "pbc": "alias",
    "Lattice": "alias",
    "cell": "alias",
    "positions": "alias",
    "arrays": {
        "numbers":
            [26, 26, 26, "..."],
        "positions":
            [[-0.10204757, -0.24557776, 0.03216429],
             [1.23818045, 1.64111918, 1.38883472],
             [-0.01367307, -0.04099747, 3.0774359],
             "..."],
        "forces":
            [[0.92008082, 1.39988003, -0.1555232],
             [1.38380678, -1.65299434, 0.55857061],
             [-0.39713156, -0.11856745, -1.23895032],
             "..."]},
    "info": {
        "cell":
            [[8.6368128, 0, 0],
             [0, 8.6368128, 0],
             [0, 0, 8.6368128]],
        "pbc": [True, True, True],
        "constraints": [],
        "config_name": "bcc_bulk_54_expanded_2_0013",
        "config_type": "bcc_bulk_54_high",
        "degauss": 0.136056917253,
        "ecutwfc": 1224.51225528,
        "energy": -186883.383046,
        "calculator_name": "unknown",
        "calculator_parameters": {},
        "kpoints": [4, 4, 4]
    }
}
