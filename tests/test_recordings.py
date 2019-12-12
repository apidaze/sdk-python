import unittest
from requests_mock import Mocker
from apidaze.http import Http
from apidaze.recordings import Recordings
import json


class TestRecordings(unittest.TestCase):
    @property
    def httpInstance(self):
        return Http(
            api_key='API_KEY',
            api_secret='API_SECRET',
            api_url='http://api.url')

    @property
    def recordings(self):
        return Recordings(self.httpInstance)

    @Mocker()
    def prepare_list(self, status_code, mocker):
        body = {
            'body': ['recording1.wav', 'recording2.wav'],
            'status_code': status_code
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

    @Mocker()
    def prepare_get(self, filename, status_code, mocker):
        body = {
            'body': 'some data',
            'status_code': status_code
        }

        mocker.register_uri(
            method='GET',
            url=f'{self.httpInstance.base_url}/recordings/{filename}',
            json=body,
            status_code=status_code
        )

        response = self.recordings.get(filename)

        self.assertEqual(json.dumps(body), response['body'].decode("utf-8"))
        self.assertEqual(status_code, response['status_code'])

    def test_get_success(self):
        self.prepare_get('name', 200)

    def test_get_failure(self):
        self.prepare_get('name', 401)

    @Mocker()
    def prepare_remove(self, filename, status_code, mocker):
        mocker.register_uri(
            method='DELETE',
            url=f'{self.httpInstance.base_url}/recordings/{filename}',
            status_code=status_code
        )

        response = self.recordings.remove(filename)

        self.assertEqual('', response['body'])
        self.assertEqual(status_code, response['status_code'])

    def test_remove_success(self):
        self.prepare_remove('name', 204)

    def test_remove_failure(self):
        self.prepare_remove('name', 401)
