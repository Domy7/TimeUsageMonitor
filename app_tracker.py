from win32gui import GetForegroundWindow
import os
import psutil
import time
import win32process
import json
from datetime import date
from database import *

class Vrijeme():
    process_time = {}
    timestamp = {}
    
    db = Database()
    db.createTable()
    today = str(date.today())

    def __init__(self):
        self.glavno()

    def petSekundi(self, oldtime):
        
        if time.time() - oldtime > 5:
            return True
        
        return False

    def save_to_database(self):
        for open_app in self.process_time:
            result = self.db.getAppInfo(self.today, open_app)
            if result:
                self.db.updateAppUsage(result[2]+5, self.today, open_app)
            else:
                self.db.insertApp(self.process_time[open_app], self.today, open_app)

    def glavno(self):
            pocetnoVrijeme = time.time()

            while True:
                current_app = psutil.Process(win32process.GetWindowThreadProcessId(GetForegroundWindow())[1]).name().replace(".exe", "")

                self.timestamp[current_app] = int(time.time())
                time.sleep(1)
                
                #gledamo ako je trenutna apk prvi put otvorena stavi vrijeme koristenja na 0
                if current_app not in self.process_time.keys():
                    self.process_time[current_app] = 0
                    
                #odnosno ako nije povecaj vrijeme kao:
                #ukupnoVr + trenutnoVr - vrijeme kada je otvorena apk zapisno u timestampu    
                self.process_time[current_app] = self.process_time[current_app]+int(time.time())-self.timestamp[current_app]
                
                #svakih 5 sekundi spremi podatke u json file    
                if self.petSekundi(pocetnoVrijeme):
                    self.save_to_database()
                    pocetnoVrijeme = time.time()
                
                print(self.process_time)

if __name__ == "__main__":
    file = open("process.log", "w")
    file.write("last PID: " + str(os.getpid()))
    file.close()
    
    Vrijeme()





