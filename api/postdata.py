import json
import requests
from datetime import datetime
import urllib3


IPADDRESS = '10.1.1.145'
PORT = '8000'
#disable pesky warnings for certificate
urllib3.disable_warnings()

#call to send vitals data to api
def send_data_to_api(obj):
    r = requests.post('https://' + IPADDRESS + ':' + PORT + '/vitalsdata/', json=obj, verify=False)
    if r.status_code == 201:
        print("Data Sent: ", r.json())
    else:
        print("Unsuccessfully with ", r.status_code)