from server.business_layers.models import WorkModel, WorkProviderModel, ProviderModel
from server.business_layers.repositories.provider_alchemy_repository import ProviderAlchemyRepository
from server.business_layers.repositories.work_alchemy_repository import WorkAlchemyRepository

work_model = WorkModel
work_provider_model = WorkProviderModel
provider_model = ProviderModel

work_repo = WorkAlchemyRepository(work_model, work_provider_model, provider_model)
provider_repo = ProviderAlchemyRepository(provider_model)
