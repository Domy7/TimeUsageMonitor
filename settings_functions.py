import os
import signal
import subprocess
# from tracemalloc import start
import win32com.client
import psutil

# provjerava je li .bat datoteku u startup folderu
def checkRunOnStartup():
    path = os.path.expanduser('~') + '\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\\run_app_tracker.bat.lnk'
    return os.path.exists(path)     # TRUE ako .bat datoteka postoji u startup folderu

# provjerava postoji li app_tracker proces kako se ne bi pokretao vise puta
def checkIfProcessIsRunning():
    return      # TRUE ako proces postoji

# funkcija stavlja .bat datoteku u startup folder
def enableRunOnStartup():
    path = os.path.expanduser('~') + '\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' + '\\run_app_tracker.bat.lnk' # apsolutna putanja do startup foldera trenutnog usera
    # path = os.path.join(start_up_folder, '\\run_app_tracker.bat.lnk') # putanja i naziv shortcuta koji ce biti napravljen
    target = os.path.dirname(__file__) + "\\run_app_tracker.bat" # putanja i naziv datoteke od koje radimo shortcut

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target

    shortcut.WindowStyle = 1 # 7 - Minimized, 3 - Maximized, 1 - Normal
    shortcut.save()

    if os.path.isfile(path):
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
    pid = int(f.read().strip("last PID: "))
    
    if psutil.pid_exists(pid) and psutil.Process(pid).name() == 'pythonw.exe':
        os.kill(int(pid), signal.SIGTERM)
        print ("Process terminated")
    else:
        print('Process doesnt exist')

# funkcija starta process apptreackera ako postoji
def startAppTracker():
    path = os.path.dirname(__file__) + "\process.log"
    f = open(path, "r")
    pid = int(f.read().strip("last PID: "))

    if psutil.pid_exists(pid) and psutil.Process(pid).name() == 'pythonw.exe':
        print("A process %s with pid %d exists" % (psutil.Process(pid).name(), pid))
        return -1

    path = os.path.dirname(__file__) + "\\run_app_tracker.bat"
    subprocess.call([path])
    print('Starting appTracker...')
