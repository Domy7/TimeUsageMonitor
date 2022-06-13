import os
import signal
import subprocess
from tracemalloc import start
import win32com.client

# funkcija stavlja .bat datoteku u startup folder
def enableRunOnStartup():
    start_up_folder = os.path.expanduser('~') + '\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' # apsolutna putanja do startup foldera trenutnog usera
    path = os.path.join(start_up_folder, 'run_app_tracker.bat.lnk') # putanja i naziv shortcuta koji ce biti napravljen
    target = os.path.dirname(__file__) + "\\run_app_tracker.bat" # putanja i naziv datoteke od koje radimo shortcut

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target

    shortcut.WindowStyle = 1 # 7 - Minimized, 3 - Maximized, 1 - Normal
    shortcut.save()

    if os.path.isfile(start_up_folder + '\\run_app_tracker.bat.lnk'):
        print("Shortcut placed")
        return 1

    print("error occured")
    return 0

# funkcija brise .bat datoteku iz startup foldera
def disableRunOnStartup():
    path = os.path.expanduser('~') + '\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' + '\\run_app_tracker.bat.lnk'

    if os.path.isfile(path):
        os.remove(path)
        print("File removed")
        return 1
    
    print("File not found")
    return 0

# funkcija gasi process apptreackera ako postoji
def terminateAppTracker():
    path = os.path.dirname(__file__) + "\process.log"
    f = open(path, "r")
    pid = f.read().strip("last PID: ")
    
    try:
        os.kill(int(pid), signal.SIGTERM)
    except OSError:
        return -1
    else:
        return int(pid)

# ne radi !!!!!!!!!!!!
def startAppTracker():
    os.startfile(os.path.dirname(__file__) + "\\run_app_tracker.bat")

startAppTracker()