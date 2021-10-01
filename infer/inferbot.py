import time
import json
from tqdm import tqdm
import matplotlib.pyplot as plt
import infer.botutils as bot
import datetime

date_format = '%Y-%m-%dT%H:%M:%SZ'

def sortDates(e):
  return e['datetime']

def isReadyToInfer(old_date, new_date):
    old = datetime.datetime.strptime(old_date, date_format)
    new = datetime.datetime.strptime(new_date, date_format)
    print(old.minute)
    print(new.minute)
    return new.minute - old.minute 

def runInferBot(data):

    Beacon_list, Beacon_points = bot.find_max_min(data)
    Beacon_list1, Beacon_points1 = bot.find_INF_points(data)

    Beacon_list3 = Beacon_list + Beacon_list1
    Beacon_list3.sort(key=sortDates)
    final_beacon_list = [i for n, i in enumerate(Beacon_list3) if i not in Beacon_list3[:n]]

    print('length of the beacon-data : ', len(Beacon_list))
    print('length of the beacon-data1 : ', len(Beacon_list1))
    print('length of the final list : ', len(final_beacon_list))
    return final_beacon_list