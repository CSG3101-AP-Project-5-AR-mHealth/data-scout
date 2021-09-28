import json
import time
import os
import datetime

from sensors.postdata import send_data_to_api
from sensors.heartsensor import HeartSensor
from sensors.tempsensor import TempSensor

DEMO_MODE = True

if DEMO_MODE:
    t_sensor = TempSensor()

def on_data(data):
      heartrate = data[7]
      temp = t_sensor.get_temp()
      now = datetime.datetime.now()
      d = now.strftime('%Y-%m-%dT%H:%M:%SZ')
      send_data_to_api({"datetime": d, "heartRate": int(heartrate), "steps": 5000, "temperature": int(temp)})


def main():
    if DEMO_MODE:
        fileObject = open('data-formatter/test_data.json', 'r')
        jsonContent = fileObject.read()
        data = json.loads(jsonContent)
        for item in data:
            send_data_to_api(item)
            time.sleep(2)
    else:        
        heartSensor = HeartSensor(on_data)

             

if __name__ == "__main__":
    main()