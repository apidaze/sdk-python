from apidaze.http import Http, HttpMethodEnum


class External_scripts(object):
    """
        Initializes the Externalscripts class

        Parameters
        ----------
        http: Http
            Apidaze Http object

        Returns
        -------
        object
            The Apidaze Externalscripts object
    """
    def __init__(self, http: Http):
        self.http = http
        self.endpoint = '/externalscripts'

    def create(self, url: str, name: str):
        """
            Creates a new external script with given id

            Parameters
            ----------
            url: str
                URL of your external script
            name: str
                Name of your external script

            Returns
            -------
            dict
                JSON response
        """

        response = self.http.request(
            method=HttpMethodEnum.POST,
            endpoint=f'{self.endpoint}',
            payload={
                'url': url,
                'name': name
            }
            )

        result = {
            'body': response.json(),
            'status_code': response.status_code
        }

        return result

    def list(self):
        """
            Shows external scripts list

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

    def get(self, id: int):
        """
            Shows specific external script by id

            Parameters
            ----------
            id: int
                id of external script

            Returns
            -------
            dict
                JSON response
        """
        response = self.http.request(
            method=HttpMethodEnum.GET,
            endpoint=f'{self.endpoint}/{id}',
            payload={}
            )

        result = {
            'body': response.json(),
            'status_code': response.status_code
        }

        return result

    def update(self, id: int, url: str, name: str):
        """
            Updates the external script with given id.

            Parameters
            ----------
            id: int
                ID of your external script
            url: str
                URL of your external script
            name: str
                Name of your external script

            Returns
            -------
            dict
                JSON response
        """
        response = self.http.request(
            method=HttpMethodEnum.PUT,
            endpoint=f'{self.endpoint}/{id}',
            payload={
                'url': url,
                'name': name
            }
            )

        result = {
            'body': response.json(),
            'status_code': response.status_code
        }

        return result

    def remove(self, id: int):
        """
            Removes specific external script with id

            Parameters
            ----------
            id: int
                id of external script

            Returns
            -------
            dict
                JSON response
        """
        response = self.http.request(
            method=HttpMethodEnum.DELETE,
            endpoint=f'{self.endpoint}/{id}',
            payload={}
            )

        result = {
            'status_code': response.status_code
        }

        return result
