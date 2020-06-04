from server.business_layers.models.base_model import BaseModel
from server.core import db


class WorkProviderModel(BaseModel):
    __tablename__ = 'work_provider'

    provider_id = db.Column(db.ForeignKey(u'provider.id'), index=True, nullable=False)
    work_id = db.Column(db.ForeignKey(u'work.id'), index=True, nullable=False)
    provider_reference = db.Column(db.Integer())
