from server.business_layers.domains.base import BaseDomain


class Work(BaseDomain):
    def __init__(self, id, iswc, title, contributors, providers=None, **kwargs):
        super().__init__(**kwargs)

        self.id = id
        self.iswc = iswc
        self.title = title
        self.contributors = contributors

        self.providers = []
        self.set_providers(providers)

    def add_provider(self, provider):
        p = WorkProvider.from_dict(provider)
        self.providers.append(p)
        return p

    def set_providers(self, providers):
        self.providers = []
        for p in providers or []:
            self.add_provider(p)


class WorkProvider(BaseDomain):

    def __init__(self, id, work_id, provider_id, provider_name, provider_reference, **kwargs):
        super().__init__(**kwargs)

        self.id = id
        self.work_id = work_id
        self.provider_id = provider_id
        self.provider_name = provider_name
        self.provider_reference = provider_reference
