import time
import json
from tqdm import tqdm

def parse_bpm(data):
    # declare lists
    X = []
    Y = []

    x=0
    for i in tqdm(data):
        temp = i['value']
        bpm = temp['bpm']
        X.append(bpm)
        Y.append(x)
        x+=1
    return X, Y


def find_max_min(X):

    RV = X
    Beacon_list  = []
    Beacon_points = []
    # print('total len: ',len(RV))

    i=1
    while i<len(RV):
        if (RV[i]["heartRate"]-RV[i-1]["heartRate"])>0:
            while (RV[i]["heartRate"]-RV[i-1]["heartRate"])>=0:
                i+=1
                if i>=len(RV):
                    break
            Beacon_points.append(i)
            Beacon_list.append(RV[i-1]) 
            
        elif (RV[i]["heartRate"]-RV[i-1]["heartRate"])<0:
            while (RV[i]["heartRate"]-RV[i-1]["heartRate"])<=0:
                
                i+=1
                if i>=len(RV):
                    break
            Beacon_points.append(i)
            Beacon_list.append(RV[i-1]) 
        else:
            i+=1

    return Beacon_list, Beacon_points
        
    

def find_INF_points(X):
    RV = X
    INF_V  = []
    Beacon_points = []
    # print('total len: ',len(RV))

    VR_Gap = 0.3
    VR = 0.1

    i = 1
    INF_V.append(RV[i])
    Beacon_points.append(i)
    j = 0
    while i<len(RV):
    #     print(j)
        if (RV[i]["heartRate"]-RV[i-1]["heartRate"])>0:
            while (RV[i]["heartRate"]-RV[i-1]["heartRate"])>=0:
                i+=1
                if i>=len(RV):
                    break
            
            i=i-1
            Beacon_points.append(i)
            INF_V.append(RV[i]) 
            j+=1
            
            if (INF_V[j]["heartRate"] - INF_V[j-1]["heartRate"]) > VR_Gap:
                # INF_V[j] = RV[INF_V[j] - INF_V[j-1]]
                pass

            if abs(RV[i]["heartRate"]-INF_V[j-1]["heartRate"])> VR*INF_V[j-1]["heartRate"]:
                INF_V[j] = RV[i]
                
            if (INF_V[j]["heartRate"] - INF_V[j-1]["heartRate"]) > VR_Gap:
                # INF_V[j] = RV[INF_V[j] - INF_V[j-1]]
                pass
            
        elif (RV[i]["heartRate"]-RV[i-1]["heartRate"])<0:
            while (RV[i]["heartRate"]-RV[i-1]["heartRate"])<=0:
                
                i+=1
                if i>=len(RV):
                    break
            i=i-1
            Beacon_points.append(i)
            INF_V.append(RV[i])
            j+=1
    #         print('j is',j)
    #         print('inf_v : ', (INF_V))
            if (INF_V[j]["heartRate"] - INF_V[j-1]["heartRate"]) > VR_Gap:
                # INF_V[j] = RV[INF_V[j] - INF_V[j-1]]
                pass

            if abs(RV[i]["heartRate"]-INF_V[j-1]["heartRate"])> VR*INF_V[j-1]["heartRate"]:
                INF_V[j] = RV[i]
                
            if (INF_V[j]["heartRate"] - INF_V[j-1]["heartRate"]) > VR_Gap:
                # INF_V[j] = RV[INF_V[j] - INF_V[j-1]]
                pass
            
        i+=1
        
    return INF_V, Beacon_points
    # print('total len: ',len(INF_V)) 
