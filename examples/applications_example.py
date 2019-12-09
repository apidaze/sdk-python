from apidaze import Client
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

apidaze = Client(api_key=API_KEY, api_secret=API_SECRET)


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


# list_subapplications()
get_app_by_id(3037)
get_app_by_key('ukkbeozt')
get_app_by_name('APPLICATION 33')
