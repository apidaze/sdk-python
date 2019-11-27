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
        self.endpoint = '/recordings'

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
            endpoint=self.endpoint,
            payload={}
            )

        result = {
            'body': response.json(),
            'status_code': response.status_code
        }

        return result

    def get(self, filename: str, description: str = ""):
        """
            Gets raw WAVE data for a recording by filename

            Parameters
            ----------
            filename: str
                Name of the recordings file.
            description: str optional
                Description of your download.

            Returns
            -------
            dict
                response, response['body'] contains the WAVE data
        """
        response = self.http.request(
            method=HttpMethodEnum.GET,
            endpoint=f'{self.endpoint}/{filename}',
            payload={
                    'name': filename,
                    'description': description
                    }
            )

        result = {
            'body': response.content,
            'status_code': response.status_code
        }

        return result

    def remove(self, filename: str):
        """
            Removes a recording by filename

            Parameters
            ----------
            filename: str
                Name of the recordings file.

            Returns
            -------
            dict
                JSON response
        """
        response = self.http.request(
            method=HttpMethodEnum.DELETE,
            endpoint=f'{self.endpoint}/{filename}',
            payload={},
            params={
                'name': filename
            }
            )

        result = {
            'body': response.text,
            'status_code': response.status_code
        }

        return result
