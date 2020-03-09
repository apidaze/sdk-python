import unittest
from requests_mock import Mocker
from apidaze.http import Http
from apidaze.sipusers import Sip_users


class TestSip_users(unittest.TestCase):
    @property
    def httpInstance(self):
        return Http(
            api_key='API_KEY',
            api_secret='API_SECRET',
            api_url='http://api.url')

    @property
    def sip_users(self):
        return Sip_users(self.httpInstance)

    @Mocker()
    def prepare_list(self, status_code, mocker):
        body = {
            'body': [{
                'id': 2517,
                'name': 'test',
                'callerid': {
                    'outboundCallerIdName': 'test',
                    'outboundCallerIdNumber': '14125423968',
                    'internalCallerIdName': 'test',
                    'internalCallerIdNumber': '1412555555'
                },
                'sip': {
                    'username': 'testUser3'
                },
                'created_at': '2020-02-14T17:32:40.000Z',
                'updated_at': '2020-02-14T17:32:40.000Z'
                },
                {
                'id': 2518,
                'name': 'test',
                'callerid': {
                    'outboundCallerIdName': 'test',
                    'outboundCallerIdNumber': '14125423968',
                    'internalCallerIdName': 'test',
                    'internalCallerIdNumber': '1412555555'
                },
                'sip': {
                    'username': 'testUser4'
                },
                'created_at': '2020-02-14T17:33:13.000Z',
                'updated_at': '2020-02-14T17:33:13.000Z'}],
            'status_code': status_code
        }

        mocker.register_uri(
            method='GET',
            url=f'{self.httpInstance.base_url}/sipusers',
            json=body,
            status_code=status_code
        )

        expected_body = {
            'body': body,
            'status_code': status_code
        }

        response = self.sip_users.list()

        self.assertEqual(expected_body, response)

    def test_list_success(self):
        self.prepare_list(200)

    def test_list_failure(self):
        self.prepare_list(401)

    @Mocker()
    def prepare_create(self, name, username, email, interrnal_id, external_id, status_code, mocker):
        body = {
            'body': {
                'id': 2529,
                'name': name,
                'callerid': {
                    'outboundCallerIdName': name,
                    'outboundCallerIdNumber': external_id,
                    'internalCallerIdName': name,
                    'internalCallerIdNumber': interrnal_id
                    },
                'sip': {
                    'username': username,
                    'password': 'test_password'
                    },
                'created_at': '2020-02-20T17:35:05.000Z',
                'updated_at': '2020-02-20T17:35:05.000Z'
            },
            'status_code': status_code
        }

        mocker.register_uri(
            method='POST',
            url=f'{self.httpInstance.base_url}/sipusers',
            json=body,
            status_code=status_code
        )

        expected_body = {
            'body': body,
            'status_code': status_code
        }

        response = self.sip_users.create(name=name, username=username, email_address=email, internal_caller_id_number=interrnal_id, external_caller_id_number=external_id)

        self.assertEqual(expected_body, response)

    def test_create_success(self):
        self.prepare_create('Test User', 'test_user', 'test@email.tld', '123', '1234567890', 201)

    def test_create_failure(self):
        self.prepare_create('Test User', 'test_user', 'test@email.tld', '123', '1234567890', 400)

    @Mocker()
    def prepare_remove(self, id, status_code, mocker):
        body = {
            'body': '',
            'status_code': status_code
        }

        mocker.register_uri(
            method='DELETE',
            url=f'{self.httpInstance.base_url}/sipusers/{id}',
            json=body,
            status_code=status_code
        )

        expected_body = {
            'body': body,
            'status_code': status_code
        }

        response = self.sip_users.remove(id)

        self.assertEqual(expected_body, response)

    def test_remove_success(self):
        self.prepare_remove(1234, 204)

    def test_remove_failure(self):
        self.prepare_remove(1234, 500)

    @Mocker()
    def prepare_get(self, id, status_code, mocker):
        body = {
            'body': {
                'id': id,
                'name': 'test',
                'callerid': {
                    'outboundCallerIdName': 'test',
                    'outboundCallerIdNumber': '14125423968',
                    'internalCallerIdName': 'test',
                    'internalCallerIdNumber': '1412555555'},
                    'sip': {
                        'username': 'testUser11'
                        },
                    'created_at': '2020-02-18T09:00:32.000Z',
                    'updated_at': '2020-02-18T09:00:32.000Z'
                },
            'status_code': status_code
        }

        mocker.register_uri(
            method='GET',
            url=f'{self.httpInstance.base_url}/sipusers/{id}',
            json=body,
            status_code=status_code
        )

        expected_body = {
            'body': body,
            'status_code': status_code
        }

        response = self.sip_users.get(id)

        self.assertEqual(expected_body, response)

    def test_get_success(self):
        self.prepare_get(1234, 200)

    def test_get_failure(self):
        self.prepare_get(1234, 401)

    @Mocker()
    def prepare_update(self, id, name, int_id, ext_id, status_code, mocker):
        body = {
            'body': {
                'id': id,
                'name': name,
                'callerid': {
                    'outboundCallerIdName': ext_id,
                    'outboundCallerIdNumber': '14125423968',
                    'internalCallerIdName': 'Test user',
                    'internalCallerIdNumber': int_id
                    },
                'sip': {
                    'username': 'testUser11',
                    'password': 'AkZVxoFXoT73NZf3'},
                    'created_at': '2020-02-18T09:00:32.000Z',
                    'updated_at': '2020-02-18T09:00:32.000Z'
                },
            'status_code': status_code
        }

        mocker.register_uri(
            method='PUT',
            url=f'{self.httpInstance.base_url}/sipusers/{id}',
            json=body,
            status_code=status_code
        )

        expected_body = {
            'body': body,
            'status_code': status_code
        }

        response = self.sip_users.update(id, name, int_id, ext_id)

        self.assertEqual(expected_body, response)

    def test_update_success(self):
        self.prepare_update(
            101,
            'Test user',
            '12312312313131',
            '45645645646464',
            202)

    def test_update_failure(self):
        self.prepare_update(
            101,
            'Test user',
            '12312312313131',
            '45645645646464',
            401)

    @Mocker()
    def prepare_status(self, id, status_code, mocker):
        body = {
            'body': {
                'uri': 'sip:test_user@voip.addr',
                'status': 'Not registered'
                },
            'status_code': status_code
        }

        mocker.register_uri(
            method='GET',
            url=f'{self.httpInstance.base_url}/sipusers/{id}/status',
            json=body,
            status_code=status_code
        )

        expected_body = {
            'body': body,
            'status_code': status_code
        }

        response = self.sip_users.status(id)

        self.assertEqual(expected_body, response)

    def test_status_success(self):
        self.prepare_status(1234, 200)

    def test_status_failure(self):
        self.prepare_status(1234, 401)

    @Mocker()
    def prepare_reset_password(self, id, status_code, mocker):
        body = {
            'body': {
                'id': id,
                'name': 'Test user',
                'callerid': {
                    'outboundCallerIdName': 'Test user',
                    'outboundCallerIdNumber': '14125423968',
                    'internalCallerIdName': 'Test user',
                    'internalCallerIdNumber': '5345353553'
                    },
                'sip': {
                    'username': 'test_user',
                    'password': 'Wupd3G6Njep4GWfw'
                    },
                'created_at': '2020-02-18T09:00:32.000Z',
                'updated_at': '2020-02-18T09:00:32.000Z'
                },
            'status_code': status_code
        }

        mocker.register_uri(
            method='POST',
            url=f'{self.httpInstance.base_url}/sipusers/{id}/password',
            json=body,
            status_code=status_code
        )

        expected_body = {
            'body': body,
            'status_code': status_code
        }

        response = self.sip_users.reset_password(id)

        self.assertEqual(expected_body, response)

    def test_reset_password_success(self):
        self.prepare_reset_password(1234, 201)

    def test_reset_password_failure(self):
        self.prepare_reset_password(1234, 400)