import unittest
from requests_mock import Mocker
from apidaze.http import Http
from apidaze.mediafiles import Mediafiles
import json


class TestMediafiles(unittest.TestCase):
    @property
    def httpInstance(self):
        return Http(
            api_key='API_KEY',
            api_secret='API_SECRET',
            api_url='http://api.url')

    @property
    def mediafiles(self):
        return Mediafiles(self.httpInstance)

    @Mocker()
    def prepare_list(self, status_code, mocker):
        body = {
            'body': ['test1.wav', 'test2.wav', 'test3.mp3', 'test4.wav', 'test5.wav'],
            'status_code': status_code
        }

        mocker.register_uri(
            method='GET',
            url=f'{self.httpInstance.base_url}/mediafiles',
            json=body,
            status_code=status_code
        )

        expected_body = {
            'body': body,
            'status_code': status_code
        }

        response = self.mediafiles.list()

        self.assertEqual(expected_body, response)

    def test_list_success(self):
        self.prepare_list(200)

    def test_list_failure(self):
        self.prepare_list(401)

    @Mocker()
    def prepare_summary(self, filename, status_code, mocker):
        headers = {
            'content-type': 'audio/wav',
            'Content-Disposition': f'inline;filename={filename}',
            'Content-Transfer-Encoding': 'binary',
            'Content-Length': '17438',
            'Date': 'Thu, 27 Feb 2020 15:01:54 GMT',
            'Connection': 'keep-alive'
        }

        body = {
            'body': "RIFF",
        }

        mocker.register_uri(
            method='HEAD',
            url=f'{self.httpInstance.base_url}/mediafiles/{filename}',
            json=body,
            status_code=status_code,
            headers=headers
        )

        expected_body = {
            'body': body,
            'headers': headers,
            'status_code': status_code
        }

        response = self.mediafiles.summary(filename)

        self.assertEqual(expected_body, response)

    def test_summary_success(self):
        self.prepare_summary('test.wav', 200)

    def test_summary_failure(self):
        self.prepare_summary('test.wav', 401)

    @Mocker()
    def prepare_get(self, filename, status_code, mocker):
        body = {
            'body': 'some data',
            'status_code': status_code
        }

        mocker.register_uri(
            method='GET',
            url=f'{self.httpInstance.base_url}/mediafiles/{filename}',
            json=body,
            status_code=status_code
        )

        expected_body = {
            'body': body,
            'status_code': status_code
        }

        response = self.mediafiles.get(filename)

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
            url=f'{self.httpInstance.base_url}/mediafiles/{filename}',
            status_code=status_code
        )

        response = self.mediafiles.remove(filename)

        self.assertEqual('', response['body'])
        self.assertEqual(status_code, response['status_code'])

    def test_remove_success(self):
        self.prepare_remove('name', 204)

    def test_remove_failure(self):
        self.prepare_remove('name', 401)