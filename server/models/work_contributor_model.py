from server.models.base_model import BaseModel
from server.core import db


class WorkContributorModel(BaseModel):
    __tablename__ = 'work_contributor'

    name = db.Column(db.String(128))

