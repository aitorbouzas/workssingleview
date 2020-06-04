from sqlalchemy.orm import relationship

from server.business_layers.models.work_provider_model import WorkProviderModel
from server.business_layers.models.base_model import BaseModel
from server.core import db


class WorkModel(BaseModel):
    __tablename__ = 'work'

    iswc = db.Column(db.String(32), index=True)
    title = db.Column(db.String(128))
    contributors = db.Column(db.String(256))

    providers = relationship(WorkProviderModel, lazy="joined")
