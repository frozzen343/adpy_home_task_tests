import unittest
import requests
from parameterized import parameterized
from app_yadisk import YaDisk

FIXTURES = [
    ('asd', 201),
    (None, 400),
]


class TestYaDisk(unittest.TestCase):
    def tearDown(self):
        """Delete created folder."""
        yadisk = YaDisk()
        url = yadisk.url + 'resources'
        headers = yadisk.get_header()
        params = {'path': 'asd'}
        return requests.delete(url, headers=headers, params=params) 

    @parameterized.expand(FIXTURES)
    def test_make_folder(self, folder, exp_result):
        yadisk = YaDisk()
        self.assertEqual(yadisk.make_folder(folder).status_code, exp_result)