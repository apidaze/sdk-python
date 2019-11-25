from apidaze.http import Http
from apidaze.messages import Messages
from apidaze.misc import Miscellaneous


class Client(object):
    def __init__(self, api_key=None, api_secret=None):
        """
        Initializes an APIdaze Client

        :param str api_key: API key to use with
        :param str api_secret: API secret to authenticate with

        :returns: APIdaze Client
        """

        self.api_key = api_key
        self.api_secret = api_secret

        if not self.api_key or not self.api_secret:
            raise ValueError('api_key and api_secret must be provided')

        # Http request
        self.http = Http(api_key=self.api_key, api_secret=self.api_secret)

        # Domains
        self.messages = Messages(http=self.http)
        self.external_scripts = None
        self.calls = None
        self.cdr_handlers = None
        self.recordings = None
        self.misc = Miscellaneous(http=self.http)
