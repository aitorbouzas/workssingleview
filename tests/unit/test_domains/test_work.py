import unittest

from server.business_layers.domains.work import Work
from tests.fixtures.json_collection import test_work


class TestWorkDomain(unittest.TestCase):
    def test_work_init(self):
        work = Work(**test_work)

        self.assertEqual(work.to_dict(), test_work)

    def test_work_from_dict(self):
        work = Work.from_dict(test_work)

        self.assertEqual(work.to_dict(), test_work)

    def test_work_to_dict(self):
        work = Work.from_dict(test_work)

        self.assertEqual(work.to_dict(), test_work)

    def test_work_equality(self):
        work = Work.from_dict(test_work)
        work2 = Work.from_dict(test_work)

        self.assertEqual(work, work2)
