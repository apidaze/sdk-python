from apidaze import Client
from apidaze.calls import CallType
import os
import time
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

apidaze = Client(api_key=API_KEY, api_secret=API_SECRET)


def place_call(origin, destination):
    response = apidaze.calls.place(
        origin,
        destination,
        destination,
        CallType.number)
    print(response)


def list_active_calls():
    response = apidaze.calls.list()
    print(response)


def get_active_call(uuid):
    response = apidaze.calls.get(uuid)
    print(response)


def terminate_call(uuid):
    response = apidaze.calls.terminate(uuid)
    print(response)


place_call(14125423968, 000000000)
time.sleep(3)
list_active_calls()
# get_active_call('')
# terminate_call('')