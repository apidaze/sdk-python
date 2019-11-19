from apidaze.http import HttpMethodEnum


class Messages(object):
    def __init__(self, http):
        self.http = http

    def sendSms(self, origin, destination, body):
        payload = {
            'to': destination,
            'from': origin,
            'body': body
        }

        response = self.http.request(
            method=HttpMethodEnum.POST,
            endpoint='/sms/send',
            payload=payload)

        result = {
            'body': response.json(),
            'status_code': response.status_code
        }

        return result
