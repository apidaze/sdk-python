from apidaze import Client
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
sandbox_url = 'https://cpaas-api.dev.voipinnovations.com'

apidaze = Client(api_key=API_KEY, api_secret=API_SECRET, api_url=sandbox_url)


def list_mediafiles(max_items: int = 500, details: bool = False,
            filter: str = "", last_token: str = ""):
    response = apidaze.media.list(max_items=max_items, details=details, filter=filter, last_token=last_token)
    print(response)

def summary(filename: str):
    response = apidaze.media.summary(filename)
    print(response)

#list_mediafiles(max_items=2, details=True)
summary('anything.wav')