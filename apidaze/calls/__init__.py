from apidaze.http import HttpMethodEnum


class Calls(object):
    def __init__(self, http):
        self.http = http

    def get_calls(self):
        response = self.http.request(
            method=HttpMethodEnum.GET,
            endpoint='/calls',
            payload={}
            )

        result = {
            'body': response.json(),
            'status_code': response.status_code
        }

        return result