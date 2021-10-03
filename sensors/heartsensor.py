from ant.easy.node import Node
from ant.easy.channel import Channel
from ant.base.message import Message

import logging
import struct
import threading
import sys
import os
import glob
import time
import datetime

from api.postdata import send_data_to_api
from sensors.tempsensor import TempSensor
import infer.inferbot as bot

NETWORK_KEY = [0xB9, 0xA5, 0x21, 0xFB, 0xBD, 0x72, 0xC3, 0x45]
t_sensor = TempSensor()
raw_data = []

def on_data(data):
    try:
        heartrate = data[7]
        temp = t_sensor.get_temp()
        now = datetime.datetime.now()
        d = now.strftime(bot.date_format)
        obj = {"datetime": d, "heartRate": int(heartrate), "steps": 0, "temperature": int(temp)}
        print("[",d,"] Heart Rate [", heartrate, "], Body Temperature [", temp, "]")
        raw_data.append(obj)
        if len(raw_data) > 1:
            if bot.isReadyToInfer(raw_data[0]["datetime"], raw_data[-1]["datetime"]):
                inferred = bot.runInferBot(raw_data)
                send_data_to_api(inferred)
                raw_data.clear()
    except Exception as e:
        print("Error:", e)
            
                

class HeartSensor:
    def __init__(self):
        node = Node()
        node.set_network_key(0x00, NETWORK_KEY)

        channel = node.new_channel(Channel.Type.BIDIRECTIONAL_RECEIVE)

        channel.on_broadcast_data = on_data
        channel.on_burst_data = on_data

        channel.set_period(8070)
        channel.set_search_timeout(12)
        channel.set_rf_freq(57)
        channel.set_id(0, 120, 0)

        try:
            channel.open()
            node.start()
        finally:
            node.stop()
        


