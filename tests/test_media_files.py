import unittest
from apidaze.http import Http
from apidaze.media_files import Media_files
from urllib3_mock import Responses
import json

responses = Responses('urllib3')


class TestMediafiles(unittest.TestCase):
    @property
    def httpInstance(self):
        return Http(
            api_key='API_KEY',
            api_secret='API_SECRET',
            api_url='http://api.url')

    @property
    def media_files(self):
        return Media_files(self.httpInstance)

    @responses.activate
    def prepare_list(self, status_code, last_token):
        body = {
            'body': ['test1.wav', 'test2.wav', 'test3.mp3', 'test4.wav', 'test5.wav'],
            'last_token': last_token,
            'status_code': status_code
        }

        responses.add(method=responses.GET,
            url=f'/API_KEY/mediafiles',
            body=json.dumps(body),
            status=status_code,
            adding_headers={'content-type': 'application/json',
            'list-truncation-token': last_token
            }
        )

        expected_body = {
            'body': body,
            'last_token': last_token,
            'status_code': status_code
        }

        response = self.media_files.list()

        self.assertEqual(expected_body, response)

    def test_list_success(self):
        self.prepare_list(200, 'vm.1cdef287.apidaze.voip/somefile.wav')

    def test_list_failure(self):
        self.prepare_list(401, 'vm.1cdef287.apidaze.voip/somefile.wav')

    @responses.activate
    def prepare_summary(self, filename, status_code):
        body = {
            'body': "RIFF",
        }

        responses.add(method=responses.HEAD,
            url=f'/API_KEY/mediafiles/{filename}',
            body=json.dumps(body),
            status=status_code
        )

        expected_body = {
            'body': body,
            'headers': {'Content-Type': 'text/plain'},
            'status_code': status_code
        }

        response = self.media_files.summary(filename)

        self.assertEqual(expected_body, response)

    def test_summary_success(self):
        self.prepare_summary('test.wav', 200)

    def test_summary_failure(self):
        self.prepare_summary('test.wav', 401)

    @responses.activate
    def prepare_get(self, filename, status_code):
        body = {
            'body': 'some data',
            'status_code': status_code
        }

        responses.add(method=responses.GET,
            url=f'/API_KEY/mediafiles/{filename}',
            body=json.dumps(body),
            status=status_code,
            adding_headers={'content-type': 'application/json'}
        )

        expected_body = {
            'body': body,
            'status_code': status_code
        }

        response = self.media_files.get(filename)

        self.assertEqual(json.dumps(body), response['body'].decode("utf-8"))
        self.assertEqual(status_code, response['status_code'])

    def test_get_success(self):
        self.prepare_get('name', 200)

    def test_get_failure(self):
        self.prepare_get('name', 401)

    @responses.activate
    def prepare_remove(self, filename, status_code):
        responses.add(method=responses.DELETE,
            url=f'/API_KEY/mediafiles/{filename}',
            status=status_code,
            adding_headers={'content-type': 'application/json'}
        )

        response = self.media_files.remove(filename)

        self.assertEqual('', response['body'])
        self.assertEqual(status_code, response['status_code'])

    def test_remove_success(self):
        self.prepare_remove('name', 204)

    def test_remove_failure(self):
        self.prepare_remove('name', 401)

    @responses.activate
    def prepare_upload(self, filename, name, status_code):
        body = {
            'body': {
                'status': f'Ok, file saved as {filename}.wav'
                },
            'status_code': status_code
        }

        responses.add(method=responses.POST,
            url=f'/API_KEY/mediafiles',
            body=json.dumps(body),
            status=status_code,
            adding_headers={'content-type': 'application/json'}
        )

        expected_body = {
            'body': body,
            'status_code': status_code
        }

        response = self.media_files.upload(filename)

        self.assertEqual(expected_body, response)

    def test_upload_success(self):
        self.prepare_upload('file', 'name', 204)

    def test_upload_failure(self):
        self.prepare_upload('file', 'name', 401)