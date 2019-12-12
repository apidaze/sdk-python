import unittest
from requests_mock import Mocker
from apidaze.http import Http
from apidaze.messages import Messages


class TestMessage(unittest.TestCase):
    @property
    def httpInstance(self):
        return Http(api_key='API_KEY', api_secret='API_SECRET', api_url='http://api.url')

    @property
    def messages(self):
        return Messages(self.httpInstance)

    @Mocker()
    def prepare_send(self, status_code, success, mocker):
        body = {
            'success': success
        }

        mocker.register_uri(
            method='POST',
            url=f'{self.httpInstance.base_url}/sms/send',
            json=body,
            status_code=status_code
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
