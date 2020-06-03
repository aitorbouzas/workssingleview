from server.business_layers.domains.work import Work
from server.business_layers.repositories.abstract_base_repository import AbstractBaseRepository


class WorkAlchemyRepository(AbstractBaseRepository):
    def __init__(self, work_model, provider_model):
        self.work_model = work_model
        self.provider_model = provider_model

    def search(self, filters, deleted=None):
        works = self.work_model.search(filters, deleted=deleted)

        search_result = []
        for w in works:
            values = w.to_dict(relations=True)
            search_result.append(Work.from_dict(values))
        return search_result

    def first(self, filters):
        search = self.search(filters)

        return search[0] if search else None

    def create(self, data):
        providers = []
        if data.get('providers'):
            providers = data.get('providers')
            del data['providers']

        work = self.work_model(**data)

        for p in providers:
            provider = self.provider_model.get(p.get('id'))
            if not provider:
                provider = self.provider_model.create(to_dict=False, **p)
            work.providers.append(provider)

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