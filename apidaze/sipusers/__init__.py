from apidaze.http import Http, HttpMethodEnum


class Sipusers(object):
    """
        Initializes the Sipusers class

        Parameters
        ----------
        http: Http
            Apidaze Http object

        Returns
        -------
        object
            The Apidaze Sipusers object
    """
    def __init__(self, http: Http):
        self.http = http
        self.endpoint = '/sipusers'

    def list(self):
        """
            Shows a list of existing SIP users

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

    def create(self, username: str, name: str,
               email_address: str,
               internal_caller_id_number: str,
               external_caller_id_number: str):
        """
            Create a SIP User for devices to register
            to Apidaze Freeswitches

            Parameters
            ----------
            username: str
                Username for the new SIP User.
            name: str
                Name for the new SIP User.
            email_address: str
                Email address for the Sip User.
            internal_caller_id_number: str
                Set as local extension
            external_caller_id_number: str
                Caller id value that will be present
                in any call requests from the registered user.

            Returns
            -------
            dict
                JSON response
        """

        response = self.http.request(
            method=HttpMethodEnum.POST,
            endpoint=f'{self.endpoint}',
            payload={
                'username': username,
                'name': name,
                'email_address': email_address,
                'internal_caller_id_number': internal_caller_id_number,
                'external_caller_id_number': external_caller_id_number
            }
            )

        result = {
            'body': response.json(),
            'status_code': response.status_code
        }

        return result

    def remove(self, id: int):
        """
            Delete a SIP User registered to an Apidaze Freeswitch.

            Parameters
            ----------
            id: int
                id of the user to delete

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
            'body': response.json() if response.text else '',
            'status_code': response.status_code
        }

        return result

    def get(self, id: int):
        """
            Shows the details of a single SIP User.

            Parameters
            ----------
            id: int
                id of the user to show details

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

    def update(self, id: int, name: str = "",
               internal_caller_id_number: str = "",
               external_caller_id_number: str = "",
               reset_password: bool = False):
        """
            Update a SIP User.

            Parameters
            ----------
            id: int
                ID of the user to update
            name: str
                Updated name for the the SIP User.
                Omit to ignore the updating of this field.
            internal_caller_id_number: int
                Updated Internal Caller ID Number for the SIP User.
                Default is an empty string; omit to ignore the updating
                of this field.
            external_caller_id_number: int
                Updated External Caller ID Number for the SIP User.
                Default is an empty string; omit to ignore the updating
                of this field.
            reset_password: bool
                If true, a new password will be generated for the SIP User.

            Returns
            -------
            dict
                JSON response
        """
        response = self.http.request(
            method=HttpMethodEnum.PUT,
            endpoint=f'{self.endpoint}/{id}',
            payload={
                'name': name,
                'internal_caller_id_number': internal_caller_id_number,
                'external_caller_id_number': external_caller_id_number,
                'reset_password': str(reset_password).lower()
            }
            )

        result = {
            'body': response.json(),
            'status_code': response.status_code
        }

        return result

    def status(self, id: int):
        """
            Show the status of a SIP User.

            Parameters
            ----------
            id: int
                id of the user to check active registration status

            Returns
            -------
            dict
                JSON response
        """
        response = self.http.request(
            method=HttpMethodEnum.GET,
            endpoint=f'{self.endpoint}/{id}/status',
            payload={}
            )

        result = {
            'body': response.json(),
            'status_code': response.status_code
        }

        return result

    def reset_password(self, id: int):
        """
            Reset the password for a SIP User.

            Parameters
            ----------
            id: int
                ID of the user to reset their password

            Returns
            -------
            dict
                JSON response
        """

        response = self.http.request(
            method=HttpMethodEnum.POST,
            endpoint=f'{self.endpoint}/{id}/password',
            payload={}
            )

        result = {
            'body': response.json(),
            'status_code': response.status_code
        }

        return result
