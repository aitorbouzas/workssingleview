from flask_testing import TestCase

from server import create_app as factory_create_app
from tests.utils.database import create, drop


class TestApiWork_v1_0(TestCase):
    def create_app(self):
        app = factory_create_app(testing=True)

        self.app = app

        self.client = app.test_client()

        self.api_version = '1.0'

        return app

    def setUp(self):
        drop(self.app)
        create(self.app)

    def tearDown(self):
        drop(self.app)

    def test_get_works(self):
        iswcs = '1234;12345'
        url = self.api_version + f'work/{iswcs}'
        self.client.get(url)
