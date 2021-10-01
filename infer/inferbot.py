import time
import json
from tqdm import tqdm
import infer.botutils as bot
import datetime

date_format = '%Y-%m-%dT%H:%M:%SZ'

def sortDates(e):
  return e['datetime']

def isReadyToInfer(old_date, new_date):
    old = datetime.datetime.strptime(old_date, date_format)
    new = datetime.datetime.strptime(new_date, date_format)
    return new.minute - old.minute 

def runInferBot(data):

    Beacon_list, Beacon_points = bot.find_max_min(data)
    Beacon_list1, Beacon_points1 = bot.find_INF_points(data)

    Beacon_list3 = Beacon_list + Beacon_list1
    Beacon_list3.sort(key=sortDates)
    final_beacon_list = [i for n, i in enumerate(Beacon_list3) if i not in Beacon_list3[:n]]

    print('Data Total length:', len(data), 'and Inferred Total length: ', len(final_beacon_list))
    return final_beacon_list