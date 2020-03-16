from apidaze import Client
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

apidaze = Client(api_key=API_KEY, api_secret=API_SECRET)


def get_recording(filename: str):
    response = apidaze.recordings.get(filename)
    data = response['body']
    file = open(filename, 'wb')
    file.write(data)
    file.close()


def remove_recording(filename: str):
    response = apidaze.recordings.remove(filename)
    print(response)


def list_recordings():
    response = apidaze.recordings.list()
    print(response)


list_recordings()
#get_recording('60d36cc6-e99f-463b-911d-c86ca4f72476.wav')
#remove_recording('60d36cc6-e99f-463b-911d-c86ca4f72476.wav')
