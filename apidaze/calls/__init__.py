from apidaze.http import HttpMethodEnum
from enum import Enum

class CallType(Enum):
    number = "number"
    sipaccount = "sipaccount"


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

    def make_call(self, caller_id, origin, destination, call_type):
        response = self.http.request(
            method=HttpMethodEnum.POST,
            endpoint='/calls',
            payload={
                'callerid': caller_id,
                'origin': origin,
                'destination': destination,
                'type': call_type.value
            }
            )

        result = {
            'body': response.json()
        }

        return result
