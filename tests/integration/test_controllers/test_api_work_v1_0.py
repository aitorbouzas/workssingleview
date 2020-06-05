import json
import os

from flask_testing import TestCase
from werkzeug.datastructures import FileStorage

from server import create_app as factory_create_app
from tests.fixtures.json_collection import test_work
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
        iswcs = 'willnotexist'
        url = self.api_version + f'/work/{iswcs}'
        response = self.client.get(url)
        self.assert404(response)

        iswcs = '1234;12345'
        url = self.api_version + f'/work/{iswcs}'
        response = self.client.get(url)
        self.assert200(response)
        # One found, one not found
        self.assertTrue(len(response.json), 1)

        # Should be like test_work
        self.assertTrue(response.json[0], test_work)

    def test_post_work(self):
        url = self.api_version + f'/work/'
        work_dict = {
            "title": "Testing Work",
            "contributors": "Myself",
            "iswc": "12345678",
            "providers": [
                {
                    "source": "Metoo",
                    "id": "32"
                }
            ]
        }
        response = self.client.post(
            url,
            data=json.dumps(work_dict),
            content_type='application/json',
        )
        self.assert200(response)

    def test_upload_csv_work(self):
        url = self.api_version + f'/work/upload'
        csv_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'works_metadata.csv')
        file = FileStorage(
            stream=open(csv_file, 'rb'),
            filename='test.csv',
            content_type='text/csv',
        )
        data = {'file': file}
        response = self.client.post(
            url,
            data=data,
            content_type='multipart/form-data',
        )
        self.assert200(response)
        self.assertEqual(len(response.json), 4)

    def test_get_csv_work(self):
        iswcs = '1234'
        url = self.api_version + f'/work/{iswcs}/csv'
        response = self.client.get(url)
        self.assert200(response)
