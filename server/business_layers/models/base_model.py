import datetime

from sqlalchemy.orm.collections import InstrumentedList

from server.core import db
from server.business_layers.models import persistence
from server.util.util import get_random_uuid


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_timestamp = db.Column(db.DateTime, nullable=False, server_default=db.text("CURRENT_TIMESTAMP"))
    updated_timestamp = db.Column(db.DateTime, nullable=False, server_default=db.text("CURRENT_TIMESTAMP"), onupdate=db.text("CURRENT_TIMESTAMP"))
    deleted_timestamp = db.Column(db.DateTime, nullable=True)

    def __init__(self, **kwargs):
        if hasattr(self, 'uuid') and 'uuid' not in kwargs:
            uuid = get_random_uuid()
            kwargs.update({'uuid': uuid})
        super().__init__(**kwargs)

    def to_dict(self, relations=False):
        tmp_obj = {}

        for column in self.__table__.columns:
            tmp_obj[column.name] = getattr(self, column.name) if hasattr(self, column.name) and getattr(self, column.name) is not None else None

        if relations:
            for attr in self.__dict__:
                if isinstance(getattr(self, attr), InstrumentedList):
                    tmp_obj[attr] = []
                    for relation in getattr(self, attr):
                        tmp_obj[attr].append(relation.to_dict())
                elif isinstance(getattr(self, attr), BaseModel):
                    tmp_obj[attr] = getattr(self, attr).to_dict()

        return tmp_obj

    def persist(self):
        persistence.add_sqlalchemy_object(self)

    def update_attributes(self, data):
        updated = False
        errored_fields = set()
        for attr, value in data.items():
            if hasattr(self, attr) and getattr(self, attr) != value and not isinstance(getattr(self, attr), (InstrumentedList,)):
                setattr(self, attr, value)
                updated = True
            else:
                errored_fields.add(attr)

        if updated:
            persistence.update_sqlalchemy_object(self)

        return updated, errored_fields

    @classmethod
    def update(cls, id, data):
        model = cls.get(id)
        if model:
            model.update_attributes(data)
            return model
        return False

    @classmethod
    def create(cls, to_dict=True, **kwargs):
        row = cls(**kwargs)
        row.persist()
        res = None
        if row:
            res = row.to_dict() if to_dict else row
        return res

    @classmethod
    def get(cls, id: int):
        row = cls.query.get(id)
        return row

    @classmethod
    def search(cls, filters, deleted=None):
        res = cls.query.filter_by(**filters if filters else {})
        if deleted and hasattr(cls, 'deleted_timestamp'):
            res.filter(db.Column('deleted_timestamp').isnot(None))
        else:
            res.filter(db.Column('deleted_timestamp').is_(None))
        return res.all()

    @classmethod
    def first(cls, filters):
        return cls.query.filter_by(**filters if filters else {}).first()

    @classmethod
    def delete(cls, id):
        """
        If an object can be marked as deleted, the object will just be marked as deleted
        If an object cannot be marked as deleted, the object will actually be deleted
        :param id:
        :return:
        """
        row = cls.get(id)
        if row:

            if hasattr(cls, 'deleted_timestamp'):
                row.update(id, {'deleted_timestamp': cls.deleted_timestamp if isinstance(cls.deleted_timestamp, datetime.datetime) else datetime.datetime.now()})
        return True if row else False

    @classmethod
    def drop(cls, id):
        row = cls.get(id)
        if row:
            persistence.delete_sqlalchemy_object(row)
        return True if row else False
