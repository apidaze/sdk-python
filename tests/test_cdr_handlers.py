import unittest
from requests_mock import Mocker
from apidaze.http import Http
from apidaze.cdrhandlers import Cdrhandlers


class TestCdrhandlers(unittest.TestCase):
    @property
    def httpInstance(self):
        return Http(api_key='API_KEY', api_secret='API_SECRET')

    @property
    def cdr_handlers(self):
        return Cdrhandlers(self.httpInstance)

    @Mocker()
    def prepare_list(self, status_code, mocker):
        body = {
            'body': [{
                'id': 101,
                'name': 'CDR Handler',
                'format': 'regular',
                'url': 'http://example.com/cdr-handler',
                'call_leg': 'inbound',
                'created_at': '2019-09-11T16:17:50.000Z',
                'updated_at': '2019-09-12T19:51:32.000Z'}],
            'status_code': status_code
        }

        mocker.register_uri(
            method='GET',
            url=f'{self.httpInstance.base_url}/cdrhttphandlers',
            json=body,
            status_code=status_code
        )

        expected_body = {
            'body': body,
            'status_code': status_code
        }

        response = self.cdr_handlers.list()

        self.assertEqual(expected_body, response)

    def test_list_success(self):
        self.prepare_list(200)

    def test_list_failure(self):
        self.prepare_list(401)