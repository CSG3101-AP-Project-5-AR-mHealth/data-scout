import json
import time
import os
import datetime

from sensors.postdata import send_data_to_api
from sensors.heartsensor import HeartSensor
from sensors.tempsensor import TempSensor

DEMO_MODE = True

def main():
    if DEMO_MODE:
        fileObject = open('data-formatter/test_data.json', 'r')
        jsonContent = fileObject.read()
        data = json.loads(jsonContent)
        for item in data:
            send_data_to_api(item)
            time.sleep(2)
    else:        
        heartSensor = HeartSensor()
        heartSensor.run()

             

if __name__ == "__main__":
    main()