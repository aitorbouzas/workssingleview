import unittest

from server.business_layers.domains.provider import Provider
from tests.fixtures.json_collection import test_provider


class TestProviderDomain(unittest.TestCase):
    def test_provider_init(self):
        provider = Provider(**test_provider)

        self.assertEqual(provider.to_dict(), test_provider)

    def test_provider_from_dict(self):
        provider = Provider.from_dict(test_provider)

        self.assertEqual(provider.to_dict(), test_provider)

    def test_provider_to_dict(self):
        provider = Provider.from_dict(test_provider)

        self.assertEqual(provider.to_dict(), test_provider)

    def test_provider_equality(self):
        provider = Provider.from_dict(test_provider)
        provider2 = Provider.from_dict(test_provider)

        self.assertEqual(provider, provider2)
