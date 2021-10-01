import json
import requests
from datetime import datetime

IPADDRESS = '10.1.1.145'
PORT = '8000'

#call to send vitals data to api
def send_data_to_api(obj):
    r = requests.post('https://' + IPADDRESS + ':' + PORT + '/vitalsdata/', json=obj, verify=False)
    print(r.json())