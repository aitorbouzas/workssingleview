from server.models.base_model import BaseModel
from server.core import db


class ProviderModel(BaseModel):
    __tablename__ = 'provider'

    name = db.Column(db.String(128))

