from apidaze import Client
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

apidaze = Client(api_key=API_KEY, api_secret=API_SECRET)

response = apidaze.messages.send(
   origin='14125423968',
   destination='14125423968',
   body='hello world from Python SDK'
)
print(response)
