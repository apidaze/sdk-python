import unittest
from requests_mock import Mocker
from apidaze.http import Http
from apidaze.applications import Applications


class TestApplications(unittest.TestCase):
    @property
    def httpInstance(self):
        return Http(
            api_key='API_KEY',
            api_secret='API_SECRET',
            api_url='http://api.url')

    @property
    def applications(self):
        return Applications(self.httpInstance)

    @Mocker()
    def prepare_list(self, status_code, mocker):
        body = {
            'body': [{
                'created_at': '2018-08-29T19:25:49.000Z',
                'updated_at': '2019-10-22T16:10:24.000Z',
                'id': 1001,
                'account_id': 1000,
                'application_id': 'qpzDicJ6',
                'api_key': 'qpzDicJ6',
                'api_secret': 'SBLOaU3jgYYu21NE4kPV798uLybhgd9d',
                'name': 'NEW APPLICATION',
                'fs_address': '8.8.8.8'
                }, {
                'created_at': '2018-08-29T19:25:49.000Z',
                'updated_at': '2019-10-22T16:10:24.000Z',
                'id': 1002,
                'account_id': 1000,
                'application_id': 'Bhy7iipf',
                'api_key': 'Bhy7iipf',
                'api_secret': 'LTaHjVTuZFWWR4pBUUrpa6cSiIJwHvwi',
                'name': 'NEW APPLICATION 2',
                'fs_address': '8.8.4.4'
                }],
            'status_code': status_code
        }

        mocker.register_uri(
            method='GET',
            url=f'{self.httpInstance.base_url}/applications',
            json=body,
            status_code=status_code
        )

        expected_body = {
            'body': body,
            'status_code': status_code
        }

        response = self.applications.list()

        self.assertEqual(expected_body, response)

    def test_list_success(self):
        self.prepare_list(200)

    def test_list_failure(self):
        self.prepare_list(401)

    @Mocker()
    def prepare_get_by_id(self, app_id, status_code, mocker):
        body = {
            'body': [{
                'created_at': '2018-08-29T19:25:49.000Z',
                'updated_at': '2019-10-22T16:10:24.000Z',
                'id': 1001,
                'account_id': 1000,
                'application_id': app_id,
                'api_key': 'qpzDicJ6',
                'api_secret': 'SBLOaU3jgYYu21NE4kPV798uLybhgd9d',
                'name': 'NEW APPLICATION',
                'fs_address': '8.8.8.8'
                }],
            'status_code': status_code
        }

        mocker.register_uri(
            method='GET',
            url=f'{self.httpInstance.base_url}/applications',
            json=body,
            status_code=status_code
        )

        expected_body = {
            'body': body,
            'status_code': status_code
        }

        response = self.applications.list()

        self.assertEqual(expected_body, response)

    def test_get_by_id_success(self):
        self.prepare_get_by_id('qpzDicJ6', 200)

    def test_get_by_id_failure(self):
        self.prepare_get_by_id('qpzDicJ6', 401)

    @Mocker()
    def prepare_get_by_key(self, api_key, status_code, mocker):
        body = {
            'body': [{
                'created_at': '2018-08-29T19:25:49.000Z',
                'updated_at': '2019-10-22T16:10:24.000Z',
                'id': 1001,
                'account_id': 1000,
                'application_id': 'qpzDicJ6',
                'api_key': api_key,
                'api_secret': 'SBLOaU3jgYYu21NE4kPV798uLybhgd9d',
                'name': 'NEW APPLICATION',
                'fs_address': '8.8.8.8'
                }],
            'status_code': status_code
        }

        mocker.register_uri(
            method='GET',
            url=f'{self.httpInstance.base_url}/applications',
            json=body,
            status_code=status_code
        )

        expected_body = {
            'body': body,
            'status_code': status_code
        }

        response = self.applications.list()

        self.assertEqual(expected_body, response)

    def test_get_by_key_success(self):
        self.prepare_get_by_key('qpzDicJ6', 200)

    def test_get_by_key_failure(self):
        self.prepare_get_by_key('qpzDicJ6', 401)

    @Mocker()
    def prepare_get_by_name(self, app_name, status_code, mocker):
        body = {
            'body': [{
                'created_at': '2018-08-29T19:25:49.000Z',
                'updated_at': '2019-10-22T16:10:24.000Z',
                'id': 1001,
                'account_id': 1000,
                'application_id': 'qpzDicJ6',
                'api_key': 'qpzDicJ6',
                'api_secret': 'SBLOaU3jgYYu21NE4kPV798uLybhgd9d',
                'name': app_name,
                'fs_address': '8.8.8.8'
                }],
            'status_code': status_code
        }

        mocker.register_uri(
            method='GET',
            url=f'{self.httpInstance.base_url}/applications',
            json=body,
            status_code=status_code
        )

        expected_body = {
            'body': body,
            'status_code': status_code
        }

        response = self.applications.list()

        self.assertEqual(expected_body, response)

    def test_get_by_name_success(self):
        self.prepare_get_by_name('my_app', 200)

    def test_get_by_name_failure(self):
        self.prepare_get_by_name('my_app', 401)
