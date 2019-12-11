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
        return self.__prepare_request()

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
        params = {
            'app_id': app_id
        }

        return self.__prepare_request(params=params)

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
        params = {
            'api_key': api_key
        }

        return self.__prepare_request(params=params)

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
        params = {
            'app_name': name
        }

        return self.__prepare_request(params=params)

    def __prepare_request(self, params: dict = {}):
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
        app_data = self.get_by_app_id(app_id=app_id)
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
        app_data = self.get_by_api_key(api_key=api_key)
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
        app_data = self.get_by_name(name=name)
        return self.__client_for_app_data(app_data=app_data['body'][0])

    def __client_for_app_data(self, app_data: dict):
        print(app_data)
        api_key = app_data['api_key']
        api_secret = app_data['api_secret']
        if not api_key or not api_secret:
            raise NameError(
                'Api Key or Api Secret are not present in the app data')

        return super(api_key=api_key, api_secret=api_secret)
