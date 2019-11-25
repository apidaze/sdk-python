from apidaze.http import Http, HttpMethodEnum


class Recordings(object):
    """
        Initializes the Recordings class

        Parameters
        ----------
        http: Http
            Apidaze Http object

        Returns
        -------
        object
            The Apidaze Recordings object
    """
    def __init__(self, http: Http):
        self.http = http

    def list(self):
        """
            Shows recordings list

            Returns
            -------
            dict
                JSON response
        """
        response = self.http.request(
            method=HttpMethodEnum.GET,
            endpoint='/recordings',
            payload={}
            )

        result = {
            'body': response.json(),
            'status_code': response.status_code
        }

        return result
