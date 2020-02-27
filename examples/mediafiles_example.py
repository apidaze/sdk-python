from apidaze import Client
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
sandbox_url = 'https://cpaas-api.dev.voipinnovations.com'

apidaze = Client(api_key=API_KEY, api_secret=API_SECRET, api_url=sandbox_url)


def list_mediafiles():
    response = apidaze.media.list()
    print(response)

list_mediafiles()