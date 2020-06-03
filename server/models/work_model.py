from sqlalchemy.orm import relationship

from server.core import db
from server.models.base_model import BaseModel
from server.models.provider_model import ProviderModel
from server.models.work_contributor_model import WorkContributorModel


class WorkProviderModel(BaseModel):
    __tablename__ = 'work_provider'

    provider_id = db.Column(db.ForeignKey(u'provider.id'), index=True, nullable=False)
    work_id = db.Column(db.ForeignKey(u'work.id'), index=True, nullable=False)


class WorkModel(BaseModel):
    __tablename__ = 'work'

    iswc = db.Column(db.String(32), unique=True, index=True)
    title = db.Column(db.String(128))

    contributors = relationship(WorkContributorModel, lazy="joined")
    providers = relationship(ProviderModel, secondary=WorkProviderModel, lazy="joined")
