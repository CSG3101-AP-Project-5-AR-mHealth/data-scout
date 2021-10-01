import json
import time
import os
import datetime

from api.postdata import send_data_to_api
from sensors.heartsensor import HeartSensor
import infer.inferbot as bot

DEMO_MODE = True

def main():
    if DEMO_MODE:
        fileObject = open('data-formatter/test_data.json', 'r')
        jsonContent = fileObject.read()
        data = json.loads(jsonContent)
        raw_data = []
        for item in data:
            raw_data.append(item)
            if len(raw_data) > 1:
                if bot.isReadyToInfer(raw_data[0]["datetime"], raw_data[-1]["datetime"]):
                    inferred = bot.runInferBot(raw_data)
                    for inferredItem in inferred:
                        send_data_to_api(inferredItem)
                    raw_data = []
            time.sleep(2)
    else:        
        heartSensor = HeartSensor()

             

if __name__ == "__main__":
    main()