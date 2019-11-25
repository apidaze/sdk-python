from apidaze import Client
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

apidaze = Client(api_key=API_KEY, api_secret=API_SECRET)

# Sending an SMS
# response = apidaze.messages.send(
#   origin='14125423968',
#   destination='14125423968',
#   body='hello world from Python SDK'
# )

# print(response)

# response = apidaze.misc.validates()

# print(response['status'])

response = apidaze.misc.validate()

print(response['body'])

response = apidaze.calls.list()

print(response)