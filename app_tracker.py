from win32gui import GetForegroundWindow
import os
import psutil
import time as t
import win32process
from datetime import date
from database import *
from win10toast import ToastNotifier



class appTracker():
    processTime = {}
    timeStamp = {}
    
    blacklist = ['explorer', 'python', 'Time Usage Monitor', 'SearchHost', 'ShellExperienceHost', 'LockApp', 'SafeTips', 'ApplicationFrameHost', 'ScpTrayApp']

    db = Database()
    today = str(date.today())
    notification = ToastNotifier()
    ALERT_BEFORE = 1

    def __init__(self):

        initialTime = t.time()
        while True:

            pidCheck = win32process.GetWindowThreadProcessId(GetForegroundWindow())[1]
            # print(type(pidCheck))
            while pidCheck < 0 and pidCheck > 4194304:
                pidCheck = win32process.GetWindowThreadProcessId(GetForegroundWindow())[1]
                print("ERROR")

            try:
                currentApp = psutil.Process(pidCheck).name().replace(".exe", "")
            except:
                print("EXCEPTION: PID = " + str(pidCheck))
                # file = open("exceptions.txt", "w")
                # file.write("EXCEPTION: PID = " + str(pidCheck))
                # file.close()

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
                    self.checkLimit(openApp, result[2])


                else:
                    self.db.insertApp(self.processTime[openApp], self.today, openApp)

    def checkLimit(self, currentApp, prcTime):
        limits = self.db.fetchLimits()
        for limit in limits:
            if limit[0] == currentApp:
                if limit[1] <= prcTime:
                    self.notification.show_toast(
                        "Time Usage Monitor",
                        "Prešli ste limit korištenja aplikacije {}. Aplikacija blokirana.".format(limit[0].capitalize()),
                        duration = 6,
                        threaded = True,
                    )
                    PROCNAME = currentApp + ".exe"
                    for proc in psutil.process_iter():
                        if proc.name() == PROCNAME:
                            proc.kill()
                print (int(limit[1]) - int(prcTime))
                if int(limit[1]) - int(prcTime) <= int(self.ALERT_BEFORE * 60 + 3) and int(limit[1]) - int(prcTime) >= int(self.ALERT_BEFORE * 60 - 3):
                    self.notification.show_toast(
                        "Time Usage Monitor",
                        "Preostalo je manje od {} min. korištenja aplikacije {}.".format(self.ALERT_BEFORE, limit[0].capitalize()),
                        duration = 6,
                        threaded = True,
                    )

if __name__ == "__main__":

    file = open("process.log", "w")
    file.write("last PID: " + str(os.getpid()))
    file.close()
    
    appTracker()
