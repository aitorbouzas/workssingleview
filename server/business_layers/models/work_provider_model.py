from server.business_layers.models.base_model import BaseModel
from server.core import db


class WorkProviderModel(BaseModel):
    __tablename__ = 'work_provider'
    __table_args__ = {'schema': 'public'}

    provider_id = db.Column(db.ForeignKey(u'public.provider.id'), index=True, nullable=False)
    work_id = db.Column(db.ForeignKey(u'public.work.id'), index=True, nullable=False)
    provider_reference = db.Column(db.Integer())
