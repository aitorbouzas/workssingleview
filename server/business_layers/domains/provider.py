from server.business_layers.domains.base import BaseDomain


class Provider(BaseDomain):
    def __init__(self, id, name, **kwargs):
        super().__init__(**kwargs)

        self.id = id
        self.name = name
