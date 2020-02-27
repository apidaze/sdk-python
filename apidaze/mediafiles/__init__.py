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

    def list(self, max_items: int = 500, details: bool = False,
             filter: str = "", last_token: str = ""):
        """
            List all Mediafiles for an application.

            Parameters
            ----------
            max_items: int
                Max number of file listings to return. If this limit is reached
                for a response, a List-Truncation-Token response header will
                contain the token to use in a subsequent call with the
                last_token property. Default 500.
            details: bool
                Include size and modified date in response data.
                Default false.
            filter: str
                Response data will only include files matching exact string
                to filter.
            last_token: str
                This should only be used if you are continuing
                a partial request. Supply the value from a previous
                request's List-Truncation-Token response header
                to continue with partitioned data.

            Returns
            -------
            dict
                JSON response
        """
        params = {
            'max_items': str(max_items),
            'filter': filter,
            'last_token': last_token,
        }
        if details:
            params.update({'details': details})

        response = self.http.request(
            method=HttpMethodEnum.GET,
            endpoint=self.endpoint,
            payload={},
            params=params
            )

        result = {
            'body': response.json(),
            'status_code': response.status_code
        }

        return result

    def get(self, filename: str):
        """
            Download a Mediafile.

            Parameters
            ----------
            filename: str
                Enter the filename with any custom pathing to stat.
                Example: test_playback_file.wav,
                clients/bob/test_playback_file.wav

            Returns
            -------
            dict
                JSON response
        """
        response = self.http.request(
            method=HttpMethodEnum.GET,
            endpoint=f'{self.endpoint}/{filename}',
            payload={}
            )

        result = {
            'body': response.content,
            'status_code': response.status_code
        }

        return result

    def summary(self, filename: str):
        """
            Show a Mediafile summary.

            Parameters
            ----------
            filename: str
                Enter the filename with any custom pathing to stat.
                Example: test_playback_file.wav,
                clients/bob/test_playback_file.wav

            Returns
            -------
            dict
                JSON response
        """
        response = self.http.request(
            method=HttpMethodEnum.HEAD,
            endpoint=f'{self.endpoint}/{filename}',
            payload={}
            )

        body = response.text
        if self.http.is_json(response.text):
            body = response.json()

        result = {
            'body': body,
            'headers': response.headers,
            'status_code': response.status_code
        }

        return result
