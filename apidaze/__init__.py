from apidaze.http import Http
from apidaze.messages import Messages
from apidaze.misc import Miscellaneous
from apidaze.calls import Calls
from apidaze.recordings import Recordings
from apidaze.cdr_handlers import Cdr_handlers
from apidaze.external_scripts import External_scripts
from apidaze.applications import Applications
from apidaze.sip_users import Sip_users


__version_info__ = ('1', '0', '0')
__version__ = '.'.join(__version_info__)

class Client(object):
    """
        Initializes the Apidaze Client class

        Parameters
        ----------
        api_key: str
            API key to use with
        api_secret: str
            API secret to authenticate with

        Returns
        -------
        object
            Apidaze Client object
    """
    def __init__(
            self,
            api_key: str = None,
            api_secret: str = None,
            api_url: str = 'https://api4.apidaze.io/'
            ):
        self.api_key = api_key
        self.api_secret = api_secret

        if not self.api_key or not self.api_secret:
            raise ValueError('api_key and api_secret must be provided')

        # Http request
        self.http = Http(
            api_key=self.api_key,
            api_secret=self.api_secret,
            api_url=api_url)

        # Domains
        self.applications = Applications(http=self.http)
        self.messages = Messages(http=self.http)
        self.external_scripts = External_scripts(http=self.http)
        self.calls = Calls(http=self.http)
        self.cdr_handlers = Cdr_handlers(http=self.http)
        self.recordings = Recordings(http=self.http)
        self.misc = Miscellaneous(http=self.http)
        self.media = None
        self.sip_users = Sip_users(http=self.http)

    def get_client_by_app_id(self, app_id: int):
        """
            Returns the Apidaze Client class based on the application id

            Parameters
            ----------
            app_id: int
                Id of the sub-application

            Returns
            -------
            object
                Apidaze Client object
        """
        app_data = self.applications.get_by_app_id(app_id=app_id)
        return self.__client_for_app_data(app_data=app_data['body'][0])

    def get_client_by_api_key(self, api_key: str):
        """
            Returns the Apidaze Client class based on the api key

            Parameters
            ----------
            api_key: str
                Api key of the sub-application

            Returns
            -------
            object
                Apidaze Client object
        """
        app_data = self.applications.get_by_api_key(api_key=api_key)
        return self.__client_for_app_data(app_data=app_data['body'][0])

    def get_client_by_name(self, name: str):
        """
            Returns the Apidaze Client class based on the application name

            Parameters
            ----------
            name: str
                Name of the sub-application

            Returns
            -------
            object
                Apidaze Client object
        """
        app_data = self.applications.get_by_name(name=name)
        return self.__client_for_app_data(app_data=app_data['body'][0])

    def __client_for_app_data(self, app_data: dict):
        api_key = app_data['api_key']
        api_secret = app_data['api_secret']
        if not api_key or not api_secret:
            raise NameError(
                'Api Key or Api Secret are not present in the app data')

        return Client(api_key=api_key, api_secret=api_secret)
