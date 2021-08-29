import os
import glob
import csv
import re
from datetime import datetime

dirPath = os.getcwd()
print(dirPath)
filesLocation = os.path.join(dirPath, 'data')
fileLocation = os.path.join(filesLocation, '*.csv')
print(fileLocation)
filenames = glob.glob(fileLocation)

print("processing ", len(filenames), "files.")


def sortOnLocalNumber(element):
    return element[1]


def conversionTo24hr(sec):
    sec_value = sec % (24 * 3600)
    hour_value = sec_value // 3600
    sec_value %= 3600
    min = sec_value // 60
    sec_value %= 60
    time = "{0}:{1}:{2}"
    return time.format(hour_value, min, sec_value)


def conversionToDate(sec):
    timestamp = sec + 631065600
    date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')
    return date

for f in filenames:
    dataList = []
    newDataList = []
    with open(f, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] != 'Type':
                    dataList.append(row)
    dataList.sort(key=sortOnLocalNumber)
    date = 0
    for row in dataList:
        if row[2] == 'device_info' and row[4] != '1':
            date = conversionToDate(int(row[4]))
        elif row[6] == 'heart_rate' and row[4] != '1':
            dateTime = conversionTo24hr(int(row[4]))
            row[4] = dateTime
            newDataList.append(row)
    print("\nFiles have been read, and it has ", len(dataList), " lines.")
    print (date)
    for row in newDataList:                      
        print (row)
