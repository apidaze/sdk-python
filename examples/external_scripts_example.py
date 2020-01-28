from apidaze import Client
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

apidaze = Client(api_key=API_KEY, api_secret=API_SECRET)


def list_external_scripts():
    response = apidaze.external_scripts.list()
    print(response)


def create_external_script(name: str, url: str):
    response = apidaze.external_scripts.create(name=name, url=url)
    print(response)


def get_external_script(id: int):
    response = apidaze.external_scripts.get(id)
    print(response)


def update_external_script(id: int, url: str, name: str):
    response = apidaze.external_scripts.update(id, url, name)
    print(response)


def remove_external_script(id: int):
    response = apidaze.external_scripts.remove(id=id)
    print(response)


list_external_scripts()
# get_external_script(1589)
# create_external_script(name='test script blabla', url='http://url.url')
# remove_external_script(1814)
# update_external_script(1589, 'http://example.com/apidaze/a.xml', 'Bartoszs script')
