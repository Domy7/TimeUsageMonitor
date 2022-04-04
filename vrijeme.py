from win32gui import GetForegroundWindow
import psutil
import time
import win32process
import json

process_time={}
timestamp = {}


def petSekundi(oldtime):
    
    if time.time() - oldtime > 5:
        return True
    
    return False

    

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
    if petSekundi(pocetnoVrijeme):
        with open('data.json', 'w') as fp:
            json.dump(process_time, fp)
        pocetnoVrijeme = time.time();
    
    print(process_time)

