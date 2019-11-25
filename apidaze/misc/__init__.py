from apidaze.http import Http, HttpMethodEnum


class Miscellaneous(object):
    """
        Initializes the Miscellaneous class

        Parameters
        ----------
        http: Http
            Apidaze Http object

        Returns
        -------
        object
            The Apidaze Miscellaneous object
    """
    def __init__(self, http: Http):
        self.http = http

    def validate(self):
        """
            Validates your API key and secret.

            Returns
            -------
            dict
                JSON response
        """
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
