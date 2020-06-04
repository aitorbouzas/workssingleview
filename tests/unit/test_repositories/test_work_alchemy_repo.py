import copy
import unittest
from unittest import mock

from server.business_layers.repositories.work_alchemy_repository import WorkAlchemyRepository
from tests.fixtures.json_collection import test_work, test_work_provider


class TestWorkAlchemyRepo(unittest.TestCase):
    def setUp(self):
        test_work_object = mock.Mock()
        test_work_object.to_dict = mock.MagicMock(return_value=test_work)
        work_list = [test_work_object]

        self.work_model = mock.MagicMock(return_value=test_work_object)
        self.work_model.create = mock.MagicMock(return_value=test_work)
        self.work_model.delete = mock.MagicMock(return_value=True)
        self.work_model.update = mock.MagicMock(return_value=test_work_object)
        self.work_model.search = mock.MagicMock(return_value=work_list)
        self.work_model.first = mock.MagicMock(return_value=test_work)
        self.work_model.get = mock.MagicMock(return_value=test_work_object)

        self.provider_model = mock.MagicMock()
        self.provider_model.get = mock.MagicMock(return_value=None)

        self.work_provider_model = mock.MagicMock()
        self.work_provider_model.create = mock.MagicMock(return_value=test_work_provider)

        self.repo = WorkAlchemyRepository(
            self.work_model,
            self.work_provider_model,
            self.provider_model,
        )

    def test_create_work_alchemy_repo(self):
        new_test_work = copy.deepcopy(test_work)
        work = self.repo.create(new_test_work)

        self.assertEqual(work.to_dict(), test_work)

    def test_delete_work_alchemy_repo(self):
        deleted = self.repo.delete(test_work.get('id'))

        self.assertTrue(deleted)

    def test_update_work(self):
        update = self.repo.update(test_work.get('id'), test_work)
        self.assertEqual(test_work, update.to_dict())

    def test_search_work(self):
        works = self.repo.search({'title': 'Shape of You'})

        self.assertEqual([work.to_dict() for work in works], [test_work])

    def test_first_work(self):
        work = self.repo.first({'iswc': '1234'})

        self.assertEqual(work.to_dict(), test_work)

    def test_add_provider(self):
        work_provider = self.repo.add_provider(test_work_provider)
        self.assertEqual(work_provider, test_work_provider)
