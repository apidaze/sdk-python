from enum import Enum
import requests
from urllib.parse import urlparse


class HttpMethodEnum(Enum):
    GET = "get"
    POST = "post"
    DELETE = "delete"
    PUT = "put"


class Http(object):
    def __init__(self, api_key: str, api_secret: str):
        self.api_key = api_key
        self.api_secret = api_secret

        if not self.api_key or not self.api_secret:
            raise ValueError('api_key and api_secret must be provided')

        # environment = 'https://api4.apidaze.io/'
        environment = 'https://cpaas-api.dev.voipinnovations.com'

        self.base_url = self.__concatenate_url(
                                environment,
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

        params = {'api_secret': self.api_secret}

        url = self.__concatenate_url(self.base_url, endpoint)

        if not self.__is_url_valid(url):
            raise ValueError('URL is invalid')

        headers = self.getHeadersWithDefault(headers=headers)
        response = None

        if params:
            params.update(params)

        if method == HttpMethodEnum.POST:
            response = requests.post(
                url, params=params, headers=headers, data=payload)
        elif method == HttpMethodEnum.GET:
            response = requests.get(
                url, params=params, headers=headers, data=payload)
        elif method == HttpMethodEnum.DELETE:
            response = requests.delete(url, params=params, headers=headers)
        elif method == HttpMethodEnum.PUT:
            response = requests.put(
                                url,
                                params=params,
                                headers=headers,
                                data=payload)

        return response

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
