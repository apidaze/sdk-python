from apidaze.http import Http, HttpMethodEnum
import os


class Media_files(object):
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

    def remove(self, filename: str):
        """
            Delete a Mediafile from an application.

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
            method=HttpMethodEnum.DELETE,
            endpoint=f'{self.endpoint}/{filename}',
            payload={}
            )

        body = response.text
        if self.http.is_json(response.text):
            body = response.json()

        result = {
            'body': body,
            'status_code': response.status_code
        }

        return result

    def upload(self, mediafile: str, name: str = None):
        """
            Upload a Mediafile for an application.
            Mediafiles can be used in playback tags by simply
            referencing the uploaded file name. WAV Files
            will be converted to 8k, 16bit, 1channel audio.
            For best quality and fastest processing,
            supply an audio file with these exact specs.

            Parameters
            ----------
            mediafile: str
                This is the file to upload.
            name: str
                The name of the file to upload. This can include
                pathing test_playback_file.wav,
                clients/bob/test_playback_file.wav, ...
                If this is not supplied, the file will be saved
                with its original name

            Returns
            -------
            dict
                JSON response
        """
        file_data = b''
        if os.path.isfile(mediafile):
            data = open(mediafile, 'rb')
            file_data = data.read()
            data.close()

        filename = name if name else os.path.basename(mediafile).split('.')[0]

        payload = {
            'mediafile': (filename, file_data, 'audio/wav'),
            'content-disposition':
                f'form-data; name="mediafile"; filename="{filename}"',
            }

        response = self.http.request(
            method=HttpMethodEnum.POST,
            endpoint=f'{self.endpoint}',
            payload=payload
            )

        result = {
            'body': response.json(),
            'status_code': response.status_code
        }

        return result
