from abc import ABCMeta, abstractmethod


class AbstractBaseRepository(metaclass=ABCMeta):
    @abstractmethod
    def search(self, filters, deleted=None):
        raise NotImplementedError

    @abstractmethod
    def create(self, data):
        raise NotImplementedError

    @abstractmethod
    def update(self, id, data):
        raise NotImplementedError

    @abstractmethod
    def delete(self, id):
        raise NotImplementedError

    @abstractmethod
    def first(self, filters):
        raise NotImplementedError
