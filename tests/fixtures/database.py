import copy

from server.business_layers.models import WorkModel, WorkProviderModel, ProviderModel, persistence
from server.business_layers.repositories.provider_alchemy_repository import ProviderAlchemyRepository
from server.business_layers.repositories.work_alchemy_repository import WorkAlchemyRepository
from server.business_layers.use_cases.work import PostWork
from tests.fixtures.json_collection import test_work


def populate():
    work_model = WorkModel
    work_provider_model = WorkProviderModel
    provider_model = ProviderModel

    provider_repo = ProviderAlchemyRepository(provider_model)
    work_repo = WorkAlchemyRepository(work_model, work_provider_model, provider_model)

    new_work = copy.deepcopy(test_work)
    post_work = PostWork(work_repo, provider_repo, new_work)
    post_work.execute()
