import unittest
from requests_mock import Mocker
from apidaze.http import Http
from apidaze.externalscripts import Externalscripts


class TestExternalScripts(unittest.TestCase):
    @property
    def httpInstance(self):
        return Http(
            api_key='API_KEY',
            api_secret='API_SECRET',
            api_url='http://api.url')

    @property
    def external_scripts(self):
        return Externalscripts(self.httpInstance)

    @Mocker()
    def prepare_list(self, status_code, mocker):
        body = {
            'body': [{
                'id': 1589,
                'name': 'Test Name',
                'url': 'http://exmaple.com/script.xml',
                'sms_url': '',
                'reseller_cust_id': 0,
                'dev_cust_id': 0,
                'created_at': '2019-09-11T15:50:10.000Z',
                'updated_at': '2019-11-25T10:31:07.000Z'}],
            'status_code': status_code
        }

        mocker.register_uri(
            method='GET',
            url=f'{self.httpInstance.base_url}/externalscripts',
            json=body,
            status_code=status_code
        )

        expected_body = {
            'body': body,
            'status_code': status_code
        }

        response = self.external_scripts.list()

        self.assertEqual(expected_body, response)

    def test_list_success(self):
        self.prepare_list(200)

    def test_list_failure(self):
        self.prepare_list(401)

    @Mocker()
    def prepare_get(self, id, status_code, mocker):
        body = {
            'body': {
                'id': id,
                'name': 'Test Name',
                'url': 'http://exmaple.com/script.xml',
                'sms_url': '',
                'reseller_cust_id': 0,
                'dev_cust_id': 0,
                'created_at': '2019-09-11T15:50:10.000Z',
                'updated_at': '2019-11-25T10:31:07.000Z'},
            'status_code': status_code
        }

        mocker.register_uri(
            method='GET',
            url=f'{self.httpInstance.base_url}/externalscripts/{id}',
            json=body,
            status_code=status_code
        )

        expected_body = {
            'body': body,
            'status_code': status_code
        }

        response = self.external_scripts.get(id)

        self.assertEqual(expected_body, response)

    def test_get_success(self):
        self.prepare_get(1234, 200)

    def test_get_failure(self):
        self.prepare_get(1234, 401)

    @Mocker()
    def prepare_update(self, id, url, name, status_code, mocker):
        body = {
            'body': {
                'id': id,
                'name': name,
                'url': url,
                'sms_url': '',
                'reseller_cust_id': 0,
                'dev_cust_id': 0,
                'created_at': '2019-09-11T15:50:10.000Z',
                'updated_at': '2019-11-28T16:42:37.000Z'},
            'status_code': status_code
        }

        mocker.register_uri(
            method='PUT',
            url=f'{self.httpInstance.base_url}/externalscripts/{id}',
            json=body,
            status_code=status_code
        )

        expected_body = {
            'body': body,
            'status_code': status_code
        }

        response = self.external_scripts.update(id, url, name)

        self.assertEqual(expected_body, response)

    def test_update_success(self):
        self.prepare_update(
            101,
            'http://exmaple.com/test.xml',
            'My Test Script',
            202)

    def test_update_failure(self):
        self.prepare_update(
            101,
            'http://exmaple.com/test.xml',
            'My Test Script',
            401)

    @Mocker()
    def prepare_create(self, url, name, status_code, mocker):
        body = {
            'body': {
                'id': '1234',
                'name': name,
                'url': url,
                'sms_url': '',
                'reseller_cust_id': 0,
                'dev_cust_id': 0,
                'created_at': '2020-01-28T14:18:31.000Z',
                'updated_at': '2020-01-28T14:18:31.000Z'},
            'status_code': status_code
        }

        mocker.register_uri(
            method='POST',
            url=f'{self.httpInstance.base_url}/externalscripts',
            json=body,
            status_code=status_code
        )

        expected_body = {
            'body': body,
            'status_code': status_code
        }

        response = self.external_scripts.create(url=url, name=name)

        self.assertEqual(expected_body, response)

    def test_create_success(self):
        self.prepare_create(
            'http://exmaple.com/test.xml',
            'My Test Script',
            201)

    def test_create_failure(self):
        self.prepare_create(
            'http://exmaple.com/test.xml',
            'My Test Script',
            401)

    @Mocker()
    def prepare_remove(self, id, status_code, mocker):
        body = {
            'status_code': status_code
        }

        mocker.register_uri(
            method='DELETE',
            url=f'{self.httpInstance.base_url}/externalscripts/{id}',
            json=body,
            status_code=status_code
        )

        expected_body = {
            'status_code': status_code
        }

        response = self.external_scripts.remove(id)

        self.assertEqual(expected_body, response)

    def test_remove_success(self):
        self.prepare_remove(1234, 204)

    def test_remove_failure(self):
        self.prepare_remove(1234, 404)
