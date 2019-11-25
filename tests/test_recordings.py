import unittest
from requests_mock import Mocker
from apidaze.http import Http
from apidaze.recordings import Recordings


class TestRecordings(unittest.TestCase):
    @property
    def httpInstance(self):
        return Http(api_key='API_KEY', api_secret='API_SECRET')

    @property
    def recordings(self):
        return Recordings(self.httpInstance)

    @Mocker()
    def prepare_list(self, status_code, mocker):
        body = {
            'body': ['recording1.wav', 'recording2.wav'],
            'status_code': 200
        }

        mocker.register_uri(
            method='GET',
            url=f'{self.httpInstance.base_url}/recordings',
            json=body,
            status_code=status_code
        )

        expected_body = {
            'body': body,
            'status_code': status_code
        }

        response = self.recordings.list()

        self.assertEqual(expected_body, response)

    def test_list_success(self):
        self.prepare_list(200)

    def test_list_failure(self):
        self.prepare_list(401)