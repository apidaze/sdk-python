from apidaze.http import Http, HttpMethodEnum


class Mediafiles(object):
    """
        Initializes the Mediafiles class

        Parameters
        ----------
        http: Http
            Apidaze Http object

        Returns
        -------
        object
            The Apidaze Mediafiles object
    """
    def __init__(self, http: Http):
        self.http = http
        self.endpoint = '/mediafiles'

    def list(self):
        """
            Shows a list of existing SIP users

            Returns
            -------
            dict
                JSON response
        """
        response = self.http.request(
            method=HttpMethodEnum.GET,
            endpoint=self.endpoint,
            payload={}
            )

        result = {
            'body': response.json(),
            'status_code': response.status_code
        }

        return result
