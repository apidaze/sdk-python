from apidaze import Client
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
sandbox_url = 'https://cpaas-api.dev.voipinnovations.com'

apidaze = Client(api_key=API_KEY, api_secret=API_SECRET, api_url=sandbox_url)


def list_sipusers():
    response = apidaze.sipusers.list()
    print(response)

def create_sipuser(username: str, 
                name: str, email_address: str,
                internal_caller_id_number: str, 
                external_caller_id_number: str):
    response = apidaze.sipusers.create(username=username,
                    name=name, email_address=email_address,
                    internal_caller_id_number=internal_caller_id_number,
                    external_caller_id_number=external_caller_id_number)
    print(response)

def remove_sipuser(id: int):
    response = apidaze.sipusers.remove(id)
    print(response)

def get_sipuser(id: int):
    response = apidaze.sipusers.get(id)
    print(response)

def update_sipuser(id: int,  name: str = "",
                internal_caller_id_number: str = "",
                external_caller_id_number: str = "",
                reset_password: bool = False):
    response = apidaze.sipusers.update(id, name, internal_caller_id_number, external_caller_id_number, reset_password)
    print(response)

def status_of_sipuser(id: int):
    response = apidaze.sipusers.status(id)
    print(response)

def reset_password(id: int):
    response = apidaze.sipusers.reset_password(id)
    print(response)

#list_sipusers()
#create_sipuser(username='bartosz_test', name='Bartosz Test User', email_address='email@email.tld', internal_caller_id_number='123', external_caller_id_number='1234567890')
#remove_sipuser(2532)
#get_sipuser(2525)
#update_sipuser(id=2525, name="Test user", internal_caller_id_number="5345353553")
#status_of_sipuser(2525)
reset_password(2525)