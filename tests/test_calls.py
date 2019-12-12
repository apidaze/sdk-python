import unittest
from requests_mock import Mocker
from apidaze.http import Http
from apidaze.calls import Calls, CallType


class TestCalls(unittest.TestCase):
    @property
    def httpInstance(self):
        return Http(api_key='API_KEY', api_secret='API_SECRET', api_url='http://api.url')

    @property
    def calls(self):
        return Calls(self.httpInstance)

    @Mocker()
    def prepare_list(self, status_code, mocker):
        body = {
            'body': {
                'uuid': '00000000-0000-0000-0000-000000000000',
                'created': '2019-11-22 11:30:03',
                'cid_name': 'Outbound Call'
                },
            'status_code': status_code
        }

        mocker.register_uri(
            method='GET',
            url=f'{self.httpInstance.base_url}/calls',
            json=body,
            status_code=status_code
        )

        expected_body = {
            'body': body,
            'status_code': status_code
        }

        response = self.calls.list()

        self.assertEqual(expected_body, response)

    def test_list_success(self):
        self.prepare_list(200)

    def test_list_failure(self):
        self.prepare_list(401)

    @Mocker()
    def prepare_place(
                        self,
                        caller_id,
                        origin,
                        destination,
                        status_code,
                        mocker):
        body = {
            'callerid': caller_id,
            'origin': origin,
            'destination': destination,
            'status_code': status_code
        }

        mocker.register_uri(
            method='POST',
            url=f'{self.httpInstance.base_url}/calls',
            json=body,
            status_code=status_code
        )

        expected_body = {
            'body': body
        }

        response = self.calls.place(
                                    caller_id,
                                    origin,
                                    destination,
                                    CallType.number)

        self.assertEqual(expected_body, response)

    def test_place_success(self):
        self.prepare_place(123456789, 987654321, 987654321, 200)

    def test_place_failure(self):
        self.prepare_place(123456789, 987654321, 987654321, 401)

    @Mocker()
    def prepare_get(self, uuid, status_code, mocker):
        body = {
            'body': {
                'uuid': uuid,
                'created': '2019-11-22 11:30:03',
                'cid_name': 'Outbound Call'
                },
            'status_code': status_code
        }

        mocker.register_uri(
            method='GET',
            url=f'{self.httpInstance.base_url}/calls/{uuid}',
            json=body,
            status_code=status_code
        )

        expected_body = {
            'body': body,
            'status_code': status_code
        }

        response = self.calls.get(uuid)

        self.assertEqual(expected_body, response)

    def test_get_success(self):
        self.prepare_get('00000000-0000-0000-0000-000000000000', 200)

    def test_get_failure(self):
        self.prepare_get('00000000-0000-0000-0000-000000000000', 401)

    @Mocker()
    def prepare_terminate(self, uuid, status_code, mocker):
        body = {
            'body': {
                'ok': ''
                },
            'status_code': status_code
        }

        mocker.register_uri(
            method='DELETE',
            url=f'{self.httpInstance.base_url}/calls/{uuid}',
            json=body,
            status_code=status_code
        )

        expected_body = {
            'body': body,
            'status_code': status_code
        }

        response = self.calls.terminate(uuid)

        self.assertEqual(expected_body, response)

    def test_terminate_success(self):
        self.prepare_terminate('00000000-0000-0000-0000-000000000000', 202)

    def test_terminate_failure(self):
        self.prepare_terminate('00000000-0000-0000-0000-000000000000', 401)
