import unittest
from apidaze.http import Http
from apidaze.cdr_handlers import Cdr_handlers
from urllib3_mock import Responses
import json

responses = Responses('urllib3')


class TestCdrhandlers(unittest.TestCase):
    @property
    def httpInstance(self):
        return Http(
            api_key='API_KEY',
            api_secret='API_SECRET',
            api_url='http://api.url')

    @property
    def cdr_handlers(self):
        return Cdr_handlers(self.httpInstance)

    @responses.activate
    def prepare_list(self, status_code):
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

        responses.add(method=responses.GET,
            url='/API_KEY/cdrhttphandlers',
            body=json.dumps(body),
            status=status_code,
            adding_headers={'content-type': 'application/json'}
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

    @responses.activate
    def prepare_create(self, url, name, status_code):
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

        responses.add(method=responses.POST,
            url='/API_KEY/cdrhttphandlers',
            body=json.dumps(body),
            status=status_code,
            adding_headers={'content-type': 'application/json'}
        )

        expected_body = {
            'body': body,
            'status_code': status_code
        }

        response = self.cdr_handlers.create(url, name)

        self.assertEqual(expected_body, response)

    def test_create_success(self):
        self.prepare_create(
                    'http://exmaple.com/cdr-handler',
                    'CDR Handler', 200)

    def test_create_failure(self):
        self.prepare_create(
            'http://exmaple.com/cdr-handler',
            'CDR Handler',
            401)

    @responses.activate
    def prepare_update(self, id, url, name, status_code):
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

        responses.add(method=responses.PUT,
            url=f'/API_KEY/cdrhttphandlers/{id}',
            body=json.dumps(body),
            status=status_code,
            adding_headers={'content-type': 'application/json'}
        )

        expected_body = {
            'body': body,
            'status_code': status_code
        }

        response = self.cdr_handlers.update(id, url, name)

        self.assertEqual(expected_body, response)

    def test_update_success(self):
        self.prepare_update(
            101,
            'http://exmaple.com/cdr-handler',
            'CDR Handler',
            202)

    def test_update_failure(self):
        self.prepare_update(
            101,
            'http://exmaple.com/cdr-handler',
            'CDR Handler',
            401)
