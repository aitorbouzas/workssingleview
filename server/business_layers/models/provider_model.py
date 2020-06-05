from server.business_layers.models.base_model import BaseModel
from server.core import db


class ProviderModel(BaseModel):
    __tablename__ = 'provider'
    __table_args__ = {'schema': 'public'}

    name = db.Column(db.String(128))
