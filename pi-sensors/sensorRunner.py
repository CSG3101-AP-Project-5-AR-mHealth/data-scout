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
import mariadb 
 
NETWORK_KEY = [0xB9, 0xA5, 0x21, 0xFB, 0xBD, 0x72, 0xC3, 0x45]

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'


#insert information 
def insert(heart_rate, body_temp):
    try: 
        conn = mariadb.connect(
            user="test",
            password="pass",
            host="localhost",
            database="vitalsdb")        
        cur = conn.cursor()
        cur.execute("INSERT INTO vitals (heart_rate, body_temp) VALUES (?, ?)", (heart_rate, body_temp)) 
        conn.commit() 
        conn.close()
    except mariadb.Error as e: 
        print(f"Error: {e}")
        print("failed to insert")

def get_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def get_temp():
    lines = get_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = get_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = (float(temp_string) / 1000.0) + 4
        return temp_c

def on_data(data):
    heartrate = data[7]
    temp = get_temp()
    now = datetime.datetime.now()
    message = str(now) + " Heartrate: " + str(heartrate) + " [BPM], Body Temp: " + str(temp) + " [Celsius]"
    print(message)
    insert(heartrate, temp)

def main():
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

if __name__ == "__main__":
    main()