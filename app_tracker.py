from sqlite3 import Timestamp
from win32gui import GetForegroundWindow
import os
import psutil
import time
import win32process
from datetime import date
from database import *

class appTracker():
    processTime = {}
    timeStamp = {}
    
    db = Database()
    db.createTable()
    today = str(date.today())

    def __init__(self):

        initialTime = time.time()
        while True:
            currentApp = psutil.Process(win32process.GetWindowThreadProcessId(GetForegroundWindow())[1]).name().replace(".exe", "")

            self.timeStamp[currentApp] = int(time.time())
            time.sleep(1)
            
            #gledamo ako je trenutna apk prvi put otvorena stavi vrijeme koristenja na 0
            if currentApp not in self.processTime.keys():
                self.processTime[currentApp] = 0
                
            #odnosno ako nije povecaj vrijeme kao:
            #ukupnoVr + trenutnoVr - vrijeme kada je otvorena apk zapisno u timestampu    
            self.processTime[currentApp] = self.processTime[currentApp]+int(time.time())-self.timeStamp[currentApp]
            
            #svakih 5 sekundi spremi podatke u json file    
            if time.time() - initialTime > 5:
                self.saveToDatabase()
                initialTime = time.time()
                self.processTime = {}
            
            print(self.processTime)       

    def saveToDatabase(self):

        for openApp in self.processTime:
            result = self.db.getAppInfo(self.today, openApp)
            if result:
                self.db.updateAppUsage(result[2] + self.processTime[openApp], self.today, openApp)
            else:
                self.db.insertApp(self.processTime[openApp], self.today, openApp)

if __name__ == "__main__":

    file = open("process.log", "w")
    file.write("last PID: " + str(os.getpid()))
    file.close()
    
    appTracker()





