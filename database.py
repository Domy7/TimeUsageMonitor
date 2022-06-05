import sqlite3
from datetime import *

#klasa za povezivanje s bazom podataka
class Database(object):
    DB_LOCATION = "./data.db"

    def __init__(self):
        self.connection = sqlite3.connect(Database.DB_LOCATION, check_same_thread=False)
        self.cur = self.connection.cursor()
        self.createTable()

    def __del__(self):
        self.connection.close()

    def allApps(self):
        self.execute('''SELECT DISTINCT app FROM usage''')
        return self.fetchAll()

    #stvaranje tablica
    def createTable(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS usage
                (date text, app text, time integer)''')
        
        self.cur.execute('''CREATE TABLE IF NOT EXISTS limits(app text, time integer)''')

    #dohvacanje aplikacija po datumu
    def fetchAppsByDate(self, date):
        self.execute('''SELECT * FROM usage WHERE date=?''', (date,))
        return self.fetchAll()
    
    #dohvacanje info o aplikaciji
    def getAppInfo(self, date, app):
        self.execute('''SELECT * FROM usage WHERE date=? AND app=?''', (date, app))
        return self.fetchOne()

    #azuriranje vremena koristenja aplikacije
    def updateAppUsage(self, time, date, app):
        self.execute('''UPDATE usage SET time=? WHERE date=? AND app=?''', (time, date, app))
        self.commit()

    #dodavanje nove aplikacije u bazu
    def insertApp(self, time, date, app):
        self.execute('''INSERT INTO usage(date,app,time) VALUES (?,?,?)''', (date, app, time))
        self.commit()

    def saveLimit(self, app, time):
        time *= 60
        self.execute('''INSERT INTO limits(app, time) VALUES(?,?)''', (app, time))
        self.commit()

    def updateLimit(self, app, time):
        time *= 60
        self.execute('''UPDATE limits SET time=? WHERE app=?''', (time, app))
        self.commit()

    def removeLimit(self, app):
        self.execute('''DELETE FROM limits WHERE app=?''', (app,))
        self.commit()

    def fetchLimits(self):
        self.execute('''SELECT * FROM limits''')
        return self.fetchAll()

    def getUsageByDate(self, date):
        self.execute('''SELECT SUM(time) FROM usage WHERE date=?''',(date,))
        return self.fetchAll()


    def fetchOne(self):
        return self.cur.fetchone()

    def fetchAll(self):
        return self.cur.fetchall()

    def execute(self, data, params=None):
        self.cur.execute(data, params or ())

    def commit(self):
        self.connection.commit()