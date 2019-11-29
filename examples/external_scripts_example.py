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


def get_external_script(id: int):
    response = apidaze.external_scripts.get(id)
    print(response)


def update_external_script(id: int, url: str, name: str):
    response = apidaze.external_scripts.update(id, url, name)
    print(response)


list_external_scripts()
get_external_script(1589)
update_external_script(1589, 'http://b.atwa.us/apidaze/b.xml', 'Bartoszs script')