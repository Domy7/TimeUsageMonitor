from win32gui import GetForegroundWindow
import psutil
import time
import win32process
import json
import os
from datetime import date
import sqlite3

process_time = {}
timestamp = {}

pocetnoVrijeme = time.time()
today = str(date.today())

#konfiguracija baze podataka
con = sqlite3.connect('data.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS usage
                (date text, app text, time integer)''')

def petSekundi(oldtime):
    if time.time() - oldtime > 5:
        return True
    
    return False

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
    
#svakih 5 sekundi azuriraj podatke u bazi    
    if petSekundi(pocetnoVrijeme):
        for open_app in process_time:
            cur.execute('''SELECT * FROM usage WHERE date=? AND app=?''',(today, open_app))
            result = cur.fetchone()
            if result:
                cur.execute('''UPDATE usage SET time=? WHERE date=? AND app=?''',(result[2]+5, today, open_app))
            else:
                cur.execute('''INSERT INTO usage(date,app,time) 
                                VALUES (?,?,?)''',(today, open_app, process_time[open_app]))
            con.commit()

        pocetnoVrijeme = time.time();
    
    print(process_time)