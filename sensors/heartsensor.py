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



class HeartSensor:
    def __init__(self, on_data):
        self.node = Node()    
        self.node.set_network_key(0x00, [0xB9, 0xA5, 0x21, 0xFB, 0xBD, 0x72, 0xC3, 0x45])
        self.channel = self.node.new_channel(Channel.Type.BIDIRECTIONAL_RECEIVE)

        self.channel.on_broadcast_data = on_data
        self.channel.on_burst_data = on_data

        self.channel.set_period(8070)
        self.channel.set_search_timeout(12)
        self.channel.set_rf_freq(57)
        self.channel.set_id(0, 120, 0)
    
    def run(self):
      try:
        self.channel.open()
        self.node.start()
      finally:
        self.node.stop()
        


