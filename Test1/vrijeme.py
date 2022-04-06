from win32gui import GetForegroundWindow
import psutil
import time
import win32process
import json
import threading


class Vrijeme(threading.Thread):
    process_time = {}
    timestamp = {}

    def petSekundi(self,oldtime):
        
        if time.time() - oldtime > 5:
            return True
        
        return False

    def glavno(self):
            #process_time = {}
            #timestamp = {}
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
                    with open('data.json', 'w') as fp:
                        json.dump(self.process_time, fp)
                    pocetnoVrijeme = time.time();
                
                print(self.process_time)






