from win32gui import GetForegroundWindow
import psutil
import time
import win32process
import json
import threading
import sqlite3
from datetime import date


con = sqlite3.connect('data.db', check_same_thread=False)
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS usage
                (date text, app text, time integer)''')

class Vrijeme(threading.Thread):
    process_time = {}
    timestamp = {}
    
    today = str(date.today())


    def petSekundi(self, oldtime):
        
        if time.time() - oldtime > 5:
            return True
        
        return False

    def save_to_database(self):
        for open_app in self.process_time:
            cur.execute('''SELECT * FROM usage WHERE date=? AND app=?''',(self.today, open_app))
            result = cur.fetchone()
            if result:
                cur.execute('''UPDATE usage SET time=? WHERE date=? AND app=?''',(result[2]+5, self.today, open_app))
            else:
                cur.execute('''INSERT INTO usage(date,app,time) 
                                VALUES (?,?,?)''',(self.today, open_app, self.process_time[open_app]))
            con.commit()

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
                    self.save_to_database()
                    pocetnoVrijeme = time.time()
                
                # print(self.process_time)






