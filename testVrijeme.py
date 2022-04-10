from win32gui import GetForegroundWindow
from collections import Counter
import psutil
import time
import win32process
import json
import os


process_time = {}
global time_diff
time_diff = {}

feeds = {}
timestamp = {}


def autoSave(oldtime):
    if time.time() - oldtime > 5:
        return True
    
    return False


global firstTime
firstTime = 1

def saveJSON():
   # if(global firstTime):
       # time_diff = dict(process_time)
       # firstTime = 0

    with open('data.json', 'r') as jfeeds:

        if os.stat('data.json').st_size == 0:
            feeds = process_time

        elif os.stat('data.json').st_size > 0:
            feeds = json.load(jfeeds)
            global time_diff
            time_diff = dict(Counter(process_time) - Counter(time_diff))
            feeds = dict(Counter(feeds) + Counter(time_diff))
            time_diff = dict(process_time)
            print(feeds)

    with open('data.json', 'w') as jupdate:
        json.dump(feeds, jupdate)


    

pocetnoVrijeme = time.time()

while True:
    current_app = psutil.Process(win32process.GetWindowThreadProcessId(GetForegroundWindow())[1]).name().replace(".exe", "")
    timestamp[current_app] = int(time.time())
    time.sleep(1)
    
#gledamo ako je trenutna apk prvi put otvorena stavi vrijeme koristenja na 0
    if current_app not in process_time.keys():
        process_time[current_app] = 0
        
#odnosno ako nije povecaj vrijeme kao:
#ukupnoVr + trenutnoVr - vrijeme kada je otvorena apk zapisno u timestampu    
    process_time[current_app] = process_time[current_app]+int(time.time())-timestamp[current_app]
    
#svakih 5 sekundi spremi podatke u json file    
    if autoSave(pocetnoVrijeme):

        saveJSON()   
        pocetnoVrijeme = time.time();
    
    #print(process_time)
