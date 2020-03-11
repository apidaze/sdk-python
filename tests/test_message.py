import unittest
from apidaze.http import Http
from apidaze.messages import Messages
from urllib3_mock import Responses
import json

responses = Responses('urllib3')


class TestMessage(unittest.TestCase):
    @property
    def httpInstance(self):
        return Http(
            api_key='API_KEY',
            api_secret='API_SECRET',
            api_url='http://api.url')

    @property
    def messages(self):
        return Messages(self.httpInstance)

    @responses.activate
    def prepare_send(self, status_code, success):
        body = {
            'success': success
        }

        responses.add(method=responses.POST,
            url='/API_KEY/sms/send',
            body=json.dumps(body),
            status=status_code,
            adding_headers={'content-type': 'application/json'}
        )

        response = self.messages.send(
            origin='123123123',
            destination='123123124',
            body='Hello world!'
        )

        expectedBody = {
            'body': body,
            'status_code': status_code
        }

        self.assertEqual(expectedBody, response)

    def test_sms_success(self):
        self.prepare_send(200, True)

    def test_sms_failure(self):
        self.prepare_send(500, False)
