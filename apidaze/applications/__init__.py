from apidaze.http import HttpMethodEnum


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

    def get_by_app_id(self, app_id: int):
        """
            Shows application with id

            Parameters
            ----------
            app_id: int
                Id of the sub-application

            Returns
            -------
            dict
                JSON response
        """
        response = self.http.request(
            method=HttpMethodEnum.GET,
            endpoint=self.endpoint,
            payload={},
            params={
                'app_id': app_id
            }
            )

        result = {
            'body': response.json(),
            'status_code': response.status_code
        }

        return result

    def get_by_api_key(self, api_key: str):
        """
            Shows application with api_key

            Parameters
            ----------
            api_key: str
                Api key of the sub-application


            Returns
            -------
            dict
                JSON response
        """
        response = self.http.request(
            method=HttpMethodEnum.GET,
            endpoint=self.endpoint,
            payload={},
            params={
                'api_key': api_key
            }
            )

        result = {
            'body': response.json(),
            'status_code': response.status_code
        }

        return result

    def get_by_name(self, name: str):
        """
            Shows application with name

            Parameters
            ----------
            name: str
                Name of the sub-application

            Returns
            -------
            dict
                JSON response
        """
        response = self.http.request(
            method=HttpMethodEnum.GET,
            endpoint=self.endpoint,
            payload={},
            params={
                'app_name': name
            }
            )

        result = {
            'body': response.json(),
            'status_code': response.status_code
        }

        return result
