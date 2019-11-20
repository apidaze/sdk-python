import unittest
from requests import Session
from requests_mock import Adapter, Mocker
from apidaze.http import Http, HttpMethodEnum


class TestHttp(unittest.TestCase):
    @property
    def httpInstance(self):
        http = Http(api_key='API_KEY', api_secret='API_SECRET')

        return http

    def test_enum_get(self):
        self.assertTrue(isinstance(HttpMethodEnum.GET, HttpMethodEnum))
        self.assertEqual(HttpMethodEnum.GET.value, 'get')

    def test_enum_post(self):
        self.assertTrue(isinstance(HttpMethodEnum.POST, HttpMethodEnum))
        self.assertEqual(HttpMethodEnum.POST.value, 'post')

    @Mocker()
    def test_request_post_success(self, mocker):
        http = self.httpInstance

        respJson = {
            'success': True
        }

        mocker.register_uri(
            method='POST',
            url=f'{http.base_url}/endpoint',
            json=respJson,
            status_code=200
        )

        response = http.request(
            method=HttpMethodEnum.POST,
            endpoint='/endpoint',
            payload={},
            headers={}
        )

        self.assertEqual(respJson, response.json())
        self.assertEqual(200, response.status_code)
