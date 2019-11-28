import unittest
from requests_mock import Mocker
from apidaze.http import Http
from apidaze.externalscripts import Externalscripts


class TestCdrhandlers(unittest.TestCase):
    @property
    def httpInstance(self):
        return Http(api_key='API_KEY', api_secret='API_SECRET')

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