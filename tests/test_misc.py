import unittest
from apidaze.http import Http
from apidaze.misc import Miscellaneous
from urllib3_mock import Responses
import json

responses = Responses('urllib3')


class TestMiscellaneous(unittest.TestCase):
    @property
    def httpInstance(self):
        return Http(
            api_key='API_KEY',
            api_secret='API_SECRET',
            api_url='http://api.url')

    @property
    def misc(self):
        return Miscellaneous(self.httpInstance)

    @responses.activate
    def prepare_validate(self, status_code):
        body = {
            'global': 'Authentication succeeded'
        }

        responses.add(method=responses.GET,
            url='/API_KEY/validates',
            body=json.dumps(body),
            status=status_code,
            adding_headers={'content-type': 'application/json'}
        )


        expected_body = {
            'body': body,
            'status_code': status_code
        }

        response = self.misc.validate()

        self.assertEqual(expected_body, response)

    def test_validates_success(self):
        self.prepare_validate(200)

    def test_validates_failure(self):
        self.prepare_validate(401)
