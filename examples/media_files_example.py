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

def summary_of_mediafile(filename: str):
    response = apidaze.media.summary(filename)
    print(response)

def download_mediafile(filename: str):
    response = apidaze.media.get(filename)
    data = response['body']
    file = open(filename, 'wb')
    file.write(data)
    file.close()
    print(response)

def remove_mediafile(filename: str):
    response = apidaze.media.remove(filename)
    print(response)

def upload_mediafile(mediafile: str, name: str = None):
    response = apidaze.media.upload(mediafile=mediafile, name=name)
    print(response)


list_mediafiles()
# summary_of_mediafile('anything.wav')
#download_mediafile('anything.wav')
# remove_mediafile('anything.wav')
# upload_mediafile(mediafile='/path/to/your/file.wav', name='optional name')