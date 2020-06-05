from server.business_layers.domains.work import Work
from server.business_layers.repositories.abstract_base_repository import AbstractBaseRepository
from server.business_layers.repositories.provider_alchemy_repository import ProviderAlchemyRepository


class WorkAlchemyRepository(AbstractBaseRepository):
    def __init__(self, work_model, work_provider_model, provider_model):
        self.work_model = work_model
        self.work_provider_model = work_provider_model
        self.provider_model = provider_model

    def search(self, filters, deleted=None):
        works = self.work_model.search(filters, deleted=deleted)

        search_result = []
        for w in works:
            values = w.to_dict(relations=True)

            # Get providers name so that the domain initializes correctly
            provider_repo = ProviderAlchemyRepository(self.provider_model)
            for p in values.get('providers'):
                provider = provider_repo.first({'id': p.get('provider_id')})
                p['provider_name'] = provider.name

            search_result.append(Work.from_dict(values))
        return search_result

    def first(self, filters):
        search = self.search(filters)

        return search[0] if search else None

    def create(self, data):
        work = self.work_model(**data)
        work.persist()
        new_work = Work.from_dict(work.to_dict())
        return new_work

    def update(self, id, data):
        update_data = self.work_model.update(id, data)
        result = None
        if update_data:
            result = Work.from_dict(update_data.to_dict())
        return result

    def delete(self, id):
        deleted = self.work_model.delete(id)
        return deleted

    def add_provider(self, data):
        work_provider = self.work_provider_model.create(**data)
        return work_provider
