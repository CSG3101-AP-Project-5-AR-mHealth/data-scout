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
            print("[",item["datetime"],"] Heart Rate [", item["heartRate"], "], Body Temperature [", item["temperature"], "]")
            raw_data.append(item)
            if len(raw_data) > 1:
                if bot.isReadyToInfer(raw_data[0]["datetime"], raw_data[-1]["datetime"]):
                    inferred = bot.runInferBot(raw_data)
                    send_data_to_api(inferred)
                    raw_data.clear()
            time.sleep(2)
    else:        
        heartSensor = HeartSensor()

             

if __name__ == "__main__":
    main()