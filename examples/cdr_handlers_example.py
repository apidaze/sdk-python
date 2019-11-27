from apidaze import Client
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

apidaze = Client(api_key=API_KEY, api_secret=API_SECRET)


def list_cdr_handlers():
    response = apidaze.cdr_handlers.list()
    print(response)


def create_cdr_handler(url: str, name: str):
    response = apidaze.cdr_handlers.create(url, name)
    print(response)


def update_cdr_handler(id: int, url: str, name: str):
    response = apidaze.cdr_handlers.update(id, url, name)
    print(response)


# create_cdr_handler('http://exmaple.com/cdr-handlers', 'CDR Handler')
# update_cdr_handler(101, 'http://example.com/cdr-handlers', 'CDR Handler')
list_cdr_handlers()