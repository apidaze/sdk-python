from apidaze.http import Http, HttpMethodEnum


class Cdrhandlers(object):
    """
        Initializes the Cdrhandlers class

        Parameters
        ----------
        http: Http
            Apidaze Http object

        Returns
        -------
        object
            The Apidaze Cdrhandlers object
    """
    def __init__(self, http: Http):
        self.http = http

    def list(self):
        """
            Shows CDR handlers list

            Returns
            -------
            dict
                JSON response
        """
        response = self.http.request(
            method=HttpMethodEnum.GET,
            endpoint='/cdrhttphandlers',
            payload={}
            )

        result = {
            'body': response.json(),
            'status_code': response.status_code
        }

        return result