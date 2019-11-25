import unittest
from requests_mock import Mocker
from apidaze.http import Http
from apidaze.misc import Miscellaneous


class TestMiscellaneous(unittest.TestCase):
    @property
    def httpInstance(self):
        return Http(api_key='API_KEY', api_secret='API_SECRET')

    @property
    def misc(self):
        return Miscellaneous(self.httpInstance)

    @Mocker()
    def prepare_validate(self, status_code, mocker):
        body = {
            'global': 'Authentication succeeded'
        }

        mocker.register_uri(
            method='GET',
            url=f'{self.httpInstance.base_url}/validates',
            json=body,
            status_code=status_code
        )

        expected_body = {
            'body': body,
            'status_code': status_code
        }

        response = self.misc.validate()

        self.assertEqual(expected_body, response)

    def test_validates_success(self):
        self.prepare_validate(200)

    def test_validates_failure(self):
        self.prepare_validate(401)
