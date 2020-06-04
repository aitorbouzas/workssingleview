import copy
import unittest
from unittest import mock

from server.business_layers.repositories.provider_alchemy_repository import ProviderAlchemyRepository
from tests.fixtures.json_collection import test_provider


class TestProviderAlchemyRepo(unittest.TestCase):
    def setUp(self):
        test_provider_object = mock.Mock()
        test_provider_object.to_dict = mock.MagicMock(return_value=test_provider)
        provider_list = [test_provider_object]

        self.provider_model = mock.MagicMock(return_value=test_provider_object)
        self.provider_model.create = mock.MagicMock(return_value=test_provider)
        self.provider_model.search = mock.MagicMock(return_value=provider_list)

        self.repo = ProviderAlchemyRepository(
            self.provider_model,
        )

    def test_create_provider_alchemy_repo(self):
        new_test_provider = copy.deepcopy(test_provider)
        provider = self.repo.create(new_test_provider)

        self.assertEqual(provider.to_dict(), test_provider)

    def test_search_provider(self):
        providers = self.repo.search({'title': 'Shape of You'})

        self.assertEqual([provider.to_dict() for provider in providers], [test_provider])
