from apidaze.http import HttpMethodEnum
from enum import Enum


class CallType(Enum):
    number = "number"
    sipaccount = "sipaccount"


class Calls(object):
    """
        Initializes the Calls class

        Parameters
        ----------
        http: Http
            Apidaze Http object

        Returns
        -------
        object
            The Apidaze Calls object
    """
    def __init__(self, http):
        self.http = http

    def list(self):
        """
            Shows active calls list

            Returns
            -------
            dict
                JSON response
        """
        response = self.http.request(
            method=HttpMethodEnum.GET,
            endpoint='/calls',
            payload={}
            )

        result = {
            'body': response.json(),
            'status_code': response.status_code
        }

        return result

    def place(self,
            caller_id: str,
            origin: str,
            destination: str,
            call_type: CallType):
        """
            Places a call to a phone number or SIP account

            Parameters
            ----------
            caller_id: str
                The phone number to present as the callerid
                (country code included, no + sign)
            origin: str
                The phone number or SIP account to ring first.
            destination: str
                The destination passed as a parameter
                to your External Script URL.
            call_type: CallType
                The type of the terminal to ring first. Options: 
                CallType.number or CallType.sipaccount.

            Returns
            -------
            dict
                JSON response
        """
        response = self.http.request(
            method=HttpMethodEnum.POST,
            endpoint='/calls',
            payload={
                'callerid': caller_id,
                'origin': origin,
                'destination': destination,
                'type': call_type.value
            }
            )

        result = {
            'body': response.json()
        }

        return result

    def get(self, uuid: str):
        """
            Shows active call with specific UUID

            Parameters
            ----------
            uuid: str
                UUID of active call

            Returns
            -------
            dict
                JSON response
        """
        response = self.http.request(
            method=HttpMethodEnum.GET,
            endpoint='/calls/'+uuid,
            payload={}
            )

        result = {
            'body': response.json(),
            'status_code': response.status_code
        }

        return result

    def terminate(self, uuid: str):
        """
            Hangs up active call with UUID

            Parameters
            ----------
            uuid: str
                UUID of active call

            Returns
            -------
            dict
                JSON response
        """
        response = self.http.request(
            method=HttpMethodEnum.DELETE,
            endpoint='/calls/'+uuid,
            payload={}
            )

        result = {
            'body': response.json(),
            'status_code': response.status_code
        }

        return result

