from apidaze.http import Http, HttpMethodEnum


class Messages(object):
    """
        Initializes the Messages class

        Parameters
        ----------
        http: Http
            Apidaze Http object

        Returns
        -------
        object
            The Apidaze Messages object
    """
    def __init__(self, http: Http):
        self.http = http

    def send(self, origin: str, destination: str, body: str):
        """
            Sends SMS to destination

            Parameters
            ----------
            origin: str
                The number to send the text from. Must be an active number on your account.
            destination: str
                Destination number (no + sign)
            body: dict
                The message to send.
        """
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
