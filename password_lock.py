import os

import bcrypt


def checkIfPassExists():    # 0 - doesn't exist, 1 - exists
    path = os.path.dirname(__file__) + '\pass.log'

    if not os.path.exists(path):
        return 0

    if os.stat(path).st_size == 0:
        return 0
    
    return 1


def createPass(pswd):       # 1 - all good
    pswd = pswd.encode('utf-8')
    hashedPswd = bcrypt.hashpw(pswd, bcrypt.gensalt(10))

    deletePass()

    path = os.path.dirname(__file__) + '\pass.log'
    f = open(path, 'wb')
    f.write(hashedPswd)
    f.close()

    return 1

# not neccessary -> createPass rewrites the file contents either way
def changePass(pswd):       # -1 - pass doesn't exist, 1 - all good
    if checkIfPassExists() == 0:
        return -1

    # change pass
    return 1


def deletePass():           # -1 - pass doesn't exist, 1 - all good
    if checkIfPassExists() == 0:
        return -1
    
    path = os.path.dirname(__file__) + '\pass.log'
    open(path, 'w').close()     # 'w' automatically deletes folders contents

    return 1


def checkIfPassCorrect(pswd):   # -1 - pass doesn't exist, 0 - incorrect, 1 - correct
    if checkIfPassExists() == 0:
        return -1
    
    path = os.path.dirname(__file__) + '\pass.log'
    f = open(path, 'rb')
    hashedPswd = f.read()
    f.close()

    pswd = pswd.encode()

    if bcrypt.checkpw(pswd, hashedPswd):
        return 1
    
    return 0
