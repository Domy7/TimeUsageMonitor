from win32gui import GetForegroundWindow
import os
import psutil
import time as t
import win32process
from datetime import date
from database import *

class appTracker():
    processTime = {}
    timeStamp = {}
    
    blacklist = ['explorer', 'python', 'Time Usage Monitor']

    db = Database()
    db.createTable()
    today = str(date.today())

    def __init__(self):

        initialTime = t.time()
        while True:
            currentApp = psutil.Process(win32process.GetWindowThreadProcessId(GetForegroundWindow())[1]).name().replace(".exe", "")

            self.timeStamp[currentApp] = int(t.time())
            t.sleep(1)
            
            #gledamo ako je trenutna apk prvi put otvorena stavi vrijeme koristenja na 0
            if currentApp not in self.processTime.keys():
                self.processTime[currentApp] = 0
                
            #odnosno ako nije povecaj vrijeme kao:
            #ukupnoVr + trenutnoVr - vrijeme kada je otvorena apk zapisno u timestampu    
            self.processTime[currentApp] = self.processTime[currentApp]+int(t.time())-self.timeStamp[currentApp]
            
            #svakih 5 sekundi spremi podatke u bazu  
            if t.time() - initialTime > 5:
                self.saveToDatabase()
                initialTime = t.time()
                self.processTime = {}
            
            
            print(self.processTime)       

    def saveToDatabase(self):
        
        for openApp in self.processTime:
            result = self.db.getAppInfo(self.today, openApp)
            if not openApp in self.blacklist:
                if result:
                    self.db.updateAppUsage(result[2] + self.processTime[openApp], self.today, openApp)
                else:
                    self.db.insertApp(self.processTime[openApp], self.today, openApp)

if __name__ == "__main__":

    file = open("process.log", "w")
    file.write("last PID: " + str(os.getpid()))
    file.close()
    
    appTracker()





