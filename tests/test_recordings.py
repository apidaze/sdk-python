import unittest
from apidaze.http import Http
from apidaze.recordings import Recordings
from urllib3_mock import Responses
import json

responses = Responses('urllib3')


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

    @responses.activate
    def prepare_list(self, status_code):
        body = {
            'body': ['recording1.wav', 'recording2.wav'],
            'status_code': status_code
        }

        responses.add(method=responses.GET,
            url='/API_KEY/recordings',
            body=json.dumps(body),
            status=status_code,
            adding_headers={'content-type': 'application/json'}
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

    @responses.activate
    def prepare_get(self, filename, status_code):
        body = {
            'body': 'some data',
            'status_code': status_code
        }

        responses.add(method=responses.GET,
            url=f'/API_KEY/recordings/{filename}',
            body=json.dumps(body),
            status=status_code,
            adding_headers={'content-type': 'application/json'}
        )

        response = self.recordings.get(filename)

        self.assertEqual(json.dumps(body), response['body'].decode("utf-8"))
        self.assertEqual(status_code, response['status_code'])

    def test_get_success(self):
        self.prepare_get('name', 200)

    def test_get_failure(self):
        self.prepare_get('name', 401)

    @responses.activate
    def prepare_remove(self, filename, status_code):
        responses.add(method=responses.DELETE,
            url=f'/API_KEY/recordings/{filename}',
            status=status_code,
            adding_headers={'content-type': 'application/json'}
        )

        response = self.recordings.remove(filename)

        self.assertEqual('', response['body'])
        self.assertEqual(status_code, response['status_code'])

    def test_remove_success(self):
        self.prepare_remove('name', 204)

    def test_remove_failure(self):
        self.prepare_remove('name', 401)
