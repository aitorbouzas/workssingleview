import copy
import unittest
from unittest import mock

from server.business_layers.domains.work import Work
from server.business_layers.use_cases.work import PostWork, UpdateWork, GetWork
from tests.fixtures.json_collection import test_work, test_work_provider


class TestWorkUseCase(unittest.TestCase):
    def setUp(self):
        self.new_test_work = copy.deepcopy(test_work)

        self.work_repo = mock.Mock()
        self.work_repo.create = mock.MagicMock(return_value=Work.from_dict(self.new_test_work))
        self.work_repo.delete = mock.MagicMock(return_value=True)
        self.work_repo.search = mock.MagicMock(return_value=[Work.from_dict(self.new_test_work)])
        self.work_repo.add_provider = mock.MagicMock(return_value=test_work_provider)
        self.work_repo.first = mock.MagicMock(return_value=Work.from_dict(self.new_test_work))
        self.work_repo.update = mock.MagicMock(return_value=Work.from_dict(self.new_test_work))

        provider_object = mock.Mock()
        provider_object.id = 1
        provider_object.name = 'Warner'

        self.provider_repo = mock.Mock()
        self.provider_repo.search = mock.MagicMock(return_value=[provider_object])
        self.provider_repo.first = mock.MagicMock(return_value=provider_object)
        self.provider_repo.create = mock.MagicMock(return_value=provider_object)

    def test_get_work(self):
        get_work_use_case = GetWork(self.work_repo, ['1234'])
        work = get_work_use_case.execute()
        self.assertEqual(work[0].to_dict(), test_work)

    def test_post_work(self):
        # Post already created one
        new_test_work = copy.deepcopy(test_work)
        post_work_use_case = PostWork(self.work_repo, self.provider_repo, new_test_work)
        work = post_work_use_case.execute()

        self.assertEqual(work.to_dict(), test_work)

        # Remock to test posting a non created work
        new_test_work = copy.deepcopy(test_work)
        new_test_work['providers'] = []
        self.work_repo.first = mock.MagicMock(return_value=None)
        self.work_repo.create = mock.MagicMock(return_value=Work.from_dict(new_test_work))

        new_test_work = copy.deepcopy(test_work)
        post_work_use_case = PostWork(self.work_repo, self.provider_repo, new_test_work)
        work = post_work_use_case.execute()

        self.assertEqual(work.to_dict(), test_work)

    def test_update_work(self):
        new_test_work = copy.deepcopy(test_work)
        new_test_work['iswc'] = None
        self.work_repo.first = mock.MagicMock(return_value=Work.from_dict(new_test_work))

        # Merge contributors
        new_test_work = copy.deepcopy(test_work)
        new_test_work['contributors'] = 'Gorillaz|Edward Sheeran'

        # Remock provider
        sony_provider = {
            'id': 2,
            'work_id': 1,
            'provider_id': 2,
            'provider_name': 'Sony',
            'provider_reference': 3,
        }
        provider_object = mock.Mock()
        provider_object.id = 2
        provider_object.name = 'Sony'
        self.provider_repo.create = mock.MagicMock(return_value=provider_object)
        self.work_repo.add_provider = mock.MagicMock(return_value=sony_provider)

        new_test_work['providers'] = [sony_provider]

        update_work_use_case = UpdateWork(test_work['id'], self.work_repo, self.provider_repo, new_test_work)
        work = update_work_use_case.execute()

        self.assertEqual(work.iswc, test_work.get('iswc'))
        self.assertEqual(work.contributors, 'Edward Sheeran|Ripoll Shakira|Gorillaz')
        self.assertEqual(len(work.providers), 2)
