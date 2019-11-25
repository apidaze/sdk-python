from apidaze.http import HttpMethodEnum


class Miscellaneous(object):
    def __init__(self, http):
        self.http = http

    def validate(self):
        response = self.http.request(
            method=HttpMethodEnum.GET,
            endpoint='/validates',
            payload={}
        )

        result = {
            'body': response.json(),
            'status_code': response.status_code
        }

        return result
