import unittest
from requests_mock import Mocker
from apidaze.http import Http, HttpMethodEnum


class TestHttp(unittest.TestCase):
    @property
    def httpInstance(self):
        return Http(api_key='API_KEY', api_secret='API_SECRET')

    @Mocker()
    def prepare_request(self, method, status_code, body, mocker):
        http = self.httpInstance

        mocker.register_uri(
            method=method,
            url=f'{http.base_url}/endpoint',
            json=body,
            status_code=status_code
        )

        response = http.request(
            method=HttpMethodEnum[method],
            endpoint='/endpoint',
            payload={},
            headers={}
        )

        self.assertEqual(body, response.json())
        self.assertEqual(status_code, response.status_code)

    def test_enum_get(self):
        self.assertTrue(isinstance(HttpMethodEnum.GET, HttpMethodEnum))
        self.assertEqual(HttpMethodEnum.GET.value, 'get')

    def test_enum_post(self):
        self.assertTrue(isinstance(HttpMethodEnum.POST, HttpMethodEnum))
        self.assertEqual(HttpMethodEnum.POST.value, 'post')

    def test_request_post_success(self):
        body = {
            'success': True
        }
        self.prepare_request('POST', 200, body)

    def test_request_post_failure(self):
        body = {
            'success': False
        }
        self.prepare_request('POST', 401, body)

    def test_request_get_success(self):
        body = {
            'success': True
        }
        self.prepare_request('GET', 200, body)

    def test_request_get_failure(self):
        body = {
            'success': False
        }
        self.prepare_request('GET', 401, body)

    def test_request_delete_success(self):
        body = {
            'success': True
        }
        self.prepare_request('DELETE', 200, body)

    def test_request_delete_failure(self):
        body = {
            'success': False
        }
        self.prepare_request('DELETE', 401, body)
