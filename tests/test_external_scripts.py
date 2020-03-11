import unittest
from apidaze.http import Http
from apidaze.external_scripts import External_scripts
from urllib3_mock import Responses
import json

responses = Responses('urllib3')


class TestExternalScripts(unittest.TestCase):
    @property
    def httpInstance(self):
        return Http(
            api_key='API_KEY',
            api_secret='API_SECRET',
            api_url='http://api.url')

    @property
    def external_scripts(self):
        return External_scripts(self.httpInstance)

    @responses.activate
    def prepare_list(self, status_code):
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

        responses.add(method=responses.GET,
            url='/API_KEY/externalscripts',
            body=json.dumps(body),
            status=status_code,
            adding_headers={'content-type': 'application/json'}
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

    @responses.activate
    def prepare_get(self, id, status_code):
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

        responses.add(method=responses.GET,
            url=f'/API_KEY/externalscripts/{id}',
            body=json.dumps(body),
            status=status_code,
            adding_headers={'content-type': 'application/json'}
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

    @responses.activate
    def prepare_update(self, id, url, name, status_code):
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

        responses.add(method=responses.PUT,
            url=f'/API_KEY/externalscripts/{id}',
            body=json.dumps(body),
            status=status_code,
            adding_headers={'content-type': 'application/json'},

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
