from apidaze import Client
from apidaze.calls import CallType
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

# response = apidaze.misc.validate()

# print(response['body'])

# response = apidaze.calls.place(14125423968, 12331213131, 12312313131, CallType.number)
# print(response)

#response = apidaze.calls.list()
#print(response)

response = apidaze.calls.terminate('b80bd938-031c-4ddf-9db9-cd4f88fc5813')
print(response)