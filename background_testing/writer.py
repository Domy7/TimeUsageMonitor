from datetime import datetime
import time
import os

if __name__ == "__main__":

    while 1:
        input = datetime.now().strftime("%H:%M:%S") + " --> Upis u bazu!" + "(PID: " + str(os.getpid()) + ")\n"
        f = open("db.txt", "a")
        f.write(input)
        f.close()

        time.sleep(5)


        

