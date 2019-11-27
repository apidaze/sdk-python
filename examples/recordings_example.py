from apidaze import Client
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

apidaze = Client(api_key=API_KEY, api_secret=API_SECRET)


def getRecording(filename: str):
    response = apidaze.recordings.get(filename)
    data = response['body']
    file = open(filename, 'wb')
    file.write(data)
    file.close()


def removeRecording(filename: str):
    response = apidaze.recordings.remove(filename)
    print(response)


def listRecordings():
    response = apidaze.recordings.list()
    print(response)


listRecordings()