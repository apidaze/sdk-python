from enum import Enum
import requests
from urllib.parse import urlparse
import json
import urllib3
import certifi
import os


class HTTPResponse(urllib3.HTTPResponse):
    def json(self):
        return json.loads(self.text)

    @property
    def status_code(self):
        return self.status

    @property
    def content(self):
        return self.data
    
    @property
    def text(self):
        return self.data.decode('utf-8') if self.data else ''


class HttpMethodEnum(Enum):
    GET = "get"
    POST = "post"
    DELETE = "delete"
    PUT = "put"


class Http(object):
    def __init__(self, api_key: str, api_secret: str, api_url: str):
        self.api_key = api_key
        self.api_secret = api_secret

        if not self.api_key or not self.api_secret:
            raise ValueError('api_key and api_secret must be provided')

        self.base_url = self.__concatenate_url(
                                api_url,
                                api_key)

    def request(
            self,
            method: HttpMethodEnum,
            endpoint: str,
            payload: dict,
            headers: dict = {},
            params: dict = {}):
        if not isinstance(method, Enum):
            raise TypeError(
                'method must be an instance of HttpMethodEnum Enum')

        local_params = {'api_secret': self.api_secret}

        url = self.__concatenate_url(self.base_url, endpoint)

        if not self.__is_url_valid(url):
            raise ValueError('URL is invalid')

        headers = self.getHeadersWithDefault(headers=headers)
        response = None

        if params:
            local_params.update(params)

        # print(f'Local params: {local_params}')

        # request = requests.Request(method.value, url, params=local_params, headers=headers, data=payload)
        # prepared = request.prepare()

        # print('{}\n{}\r\n{}\r\n\r\n{}'.format(
        # '-----------START-----------',
        # prepared.method + ' ' + prepared.url,
        # '\r\n'.join('{}: {}'.format(k, v) for k, v in prepared.headers.items()),
        # prepared.body,
        # ))


        # session = requests.Session()
        # response = session.send(prepared)

        # if method == HttpMethodEnum.POST:
        #     response = requests.post(
        #         url, params=local_params, headers=headers, data=payload,
        #         files=files)
        # elif method == HttpMethodEnum.GET:
        #     response = requests.get(
        #         url, params=local_params, headers=headers, data=payload)
        # elif method == HttpMethodEnum.DELETE:
        #     response = requests.delete(
        #         url,
        #         params=local_params,
        #         headers=headers)
        # elif method == HttpMethodEnum.PUT:
        #     response = requests.put(
        #                         url,
        #                         params=local_params,
        #                         headers=headers,
        #                         data=payload)
        # elif method == HttpMethodEnum.HEAD:
        #     response = requests.head(
        #         url, params=local_params, headers=headers, data=payload)

        if payload:
            local_params.update(payload)

        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where(), num_pools=2)
        response = http.request(
            method.value,
            url,
            fields=local_params,
            headers=headers
            )

        return HTTPResponse(body=response.data, headers=response.headers, status=response.status, reason=response.reason, msg=response.msg)

    def getHeadersWithDefault(self, headers={}):
        default = {
            'content-type': 'application/x-www-form-urlencoded'
        }

        default.update(headers)

        return default

    def __is_url_valid(self, url: str) -> bool:
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc, result.path])
        except ValueError:
            return False

    def __slash_join(self, *args: str):
        return "/".join(arg.strip("/") for arg in args)

    def __concatenate_url(self, url: str, endpoint: str) -> str:
        return self.__slash_join(url, endpoint)
