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
        self.endpoint = '/cdrhttphandlers'

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
            endpoint=self.endpoint,
            payload={}
            )

        result = {
            'body': response.json(),
            'status_code': response.status_code
        }

        return result

    def create(self, url: str, name: str):
        """
            Creates a new CDR HTTP Handler. 
            This will post the call detail (after a call) to the webhook URL you define.

            Parameters
            ----------
            url: str
                URL. of your application
            name: str
                Your App name

            Returns
            -------
            dict
                JSON response
        """
        response = self.http.request(
            method=HttpMethodEnum.POST,
            endpoint=self.endpoint,
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

    def update(self, id: int, url: str, name: str):
        """
            Updates your current CDR HTTP Handler. 

            Parameters
            ----------
            id: int
                ID of your CDR handler
            url: str
                URL. of your application
            name: str
                Your App name

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