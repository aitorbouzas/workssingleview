from server.business_layers.repositories.abstract_base_repository import AbstractBaseRepository


class ProviderAlchemyRepository(AbstractBaseRepository):
    def __init__(self, provider_model):
        self.provider_model = provider_model

    def delete(self, id):
        raise NotImplementedError

    def first(self, filters):
        raise NotImplementedError

    def update(self, id, data):
        raise NotImplementedError

    def search(self, filters, deleted=None):
        providers = self.provider_model.search(filters, deleted=deleted)
        return providers

    def create(self, data):
        provider = self.provider_model(**data)
        provider.persist()
        return provider
