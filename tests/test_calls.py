import unittest
from requests_mock import Mocker
from apidaze.http import Http
from apidaze.calls import Calls


class TestCalls(unittest.TestCase):
    @property
    def httpInstance(self):
        return Http(api_key='API_KEY', api_secret='API_SECRET')

    @property
    def calls(self):
        return Calls(self.httpInstance)

    @Mocker()
    def prepare_get_calls(self, status_code, mocker):
        body = {
            'body': {
                'uuid': '00000000-0000-0000-0000-000000000000',
                'created': '2019-11-22 11:30:03',
                'cid_name': 'Outbound Call'
                },
            'status_code': 200
        }

        mocker.register_uri(
            method='GET',
            url=f'{self.httpInstance.base_url}/calls',
            json=body,
            status_code=status_code
        )

        expected_body = {
            'body': body,
            'status_code': status_code
        }

        response = self.calls.get_calls()

        self.assertEqual(expected_body, response)

    def test_get_calls_success(self):
        self.prepare_get_calls(200)

    def test_get_calls_failure(self):
        self.prepare_get_calls(401)