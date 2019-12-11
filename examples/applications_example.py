from apidaze import Client
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
sandbox_url = 'https://cpaas-api.dev.voipinnovations.com'

apidaze = Client(api_key=API_KEY, api_secret=API_SECRET, api_url=sandbox_url)


def list_subapplications():
    response = apidaze.applications.list()
    print(response)


def get_app_by_id(app_id):
    response = apidaze.applications.get_by_app_id(app_id)
    print(response)


def get_app_by_key(api_key):
    response = apidaze.applications.get_by_api_key(api_key)
    print(response)


def get_app_by_name(name):
    response = apidaze.applications.get_by_name(name)
    print(response)


def client_by_id(app_id):
    return apidaze.get_client_by_app_id(app_id=app_id)


def client_by_key(api_key):
    return apidaze.get_client_by_api_key(api_key=api_key)


def client_by_name(name):
    return apidaze.get_client_by_name(name=name)


# list_subapplications()
# get_app_by_id(3037)
# get_app_by_key('ukkbeozt')
# get_app_by_name('APPLICATION 33')

print(client_by_id(3037))
print(client_by_key('ukkbeozt'))
print(client_by_name('APPLICATION 33'))
