from apidaze.http import Http, HttpMethodEnum


class Applications(object):
    """
        Initializes the Applications class

        Parameters
        ----------
        http: Http
            Apidaze Http object

        Returns
        -------
        object
            The Apidaze Applications object
    """
    def __init__(self, http):
        self.http = http
        self.endpoint = '/applications'

    def list(self):
        """
            Shows sub-applications list

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

    # def get(id: int):

    # def get(api_key: str):

    # def get(name: str):
