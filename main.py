import sys
# import os
from venv import create

# from bs4 import Stylesheet
from ui_gui import *
from qt_material import *

# import icons_rc
from chart import *
from bar import *
from database import *
from PySide2.QtGui import *

from datetime import date

today = str(date.today())
db = Database()
db.createTable()

class MainWindow(QMainWindow):
    
    def __init__(self, parent = None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.centralWidget.setCurrentWidget(self.ui.stats_page)

        # fetching previously set limits from db
        apps = db.fetchLimits()

        # initializing limit dictionary
        self.limitsDict = dict()


        for apk in apps:
            self.limitsDict[apk[0]] = apk[1] // 60


        # adding apps to dropdown menu
        allApps = db.allApps()

        for apk in allApps:
            self.ui.choose_app.addItem(apk[0])


        self.showLimits()


        self.ui.choose_time_h.setMaximum(23)
        self.ui.choose_time_m.setMaximum(59)

        # init chart, bar
        self.data = db.fetchAppsByDate(today)
        self.chart = Chart(self.ui, self.data)
        self.bar = Bar(self.ui)

        # load stylesheet, overrides fonts set in QTdesigner
        apply_stylesheet(app, theme='light_blue.xml')
        
        # removes window title bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # sets main background to transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # shadow effect style
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 550))

        # applies shadow to centrtal widget
        self.ui.centralWidget.setGraphicsEffect(self.shadow)
        
        # sets window icon and title
        #self.setWindowIcon(QtGui.QIcon("path"))
        self.setWindowTitle("TimeUsageMonitor")

        # resize window
        QSizeGrip(self.ui.size_grip)

        self.ui.minimize_button.clicked.connect(lambda: self.showMinimized())
        self.ui.exit_button.clicked.connect(lambda: self.close())
        self.ui.resize_button.clicked.connect(lambda: self.restoreOrMaximizeWindow())

        # menu buttons
        self.ui.stats_btn.clicked.connect(lambda: self.ui.centralWidget.setCurrentWidget(self.ui.stats_page))
        self.ui.lock_btn.clicked.connect(lambda: self.ui.centralWidget.setCurrentWidget(self.ui.lock_page))
        self.ui.settings_btn.clicked.connect(lambda: self.ui.centralWidget.setCurrentWidget(self.ui.settings_page))
        self.ui.data_btn.clicked.connect(lambda: self.ui.centralWidget.setCurrentWidget(self.ui.data_page))

        # refresh button, stats tab
        self.ui.refresh_chart_btn.clicked.connect(lambda: self.refreshPieChart())

        # self.ui.header_frame.mouseMoveEvent = self.moveWindow
        self.ui.header_center_fr.mouseMoveEvent = self.moveWindow
        
        # TODO: opens menu
        #self.ui.menu_btn.clicked.connect(lambda: self.openMenu())

        self.ui.submit_limit.clicked.connect(lambda: self.submitLimit())


    def submitLimit(self):

        tmpApp = ""
        tmpTime = 0
        
        tmpApp = self.ui.choose_app.currentText()                                           # reads chosen app
        tmpTime = self.ui.choose_time_h.value() * 60 + self.ui.choose_time_m.value()        # reads chosen time in minutes


        if (not self.limitsDict.keys() or not tmpApp in self.limitsDict.keys()) and tmpTime:        # checks if dictionary is empty and if specified app already exists in the dict
            self.limitsDict[tmpApp] = tmpTime
            db.saveLimit(tmpApp, tmpTime)           # save data to db
        elif tmpApp in self.limitsDict.keys():      # if app (exists and) already has a limit (changes it)
            self.limitsDict[tmpApp] = tmpTime       # change the time for that index
            db.updateLimit(tmpApp, tmpTime)

            if not tmpTime:                     # if chosen time is 0, deletes the limit
                self.limitsDict.pop(tmpApp)
                db.removeLimit(tmpApp)
                                                # will not add a limit if app doesn't already have one and the set time is 0

        self.showLimits()
    

    def showLimits(self):
        self.item = []

        for app in self.limitsDict.keys():
            self.item.append(app + " " + str(self.limitsDict[app] // 60) + "h " + str(self.limitsDict[app] % 60) + "m")


        self.listWidget = QListWidget(self.ui.limits_list)
        self.listWidget.addItems(self.item)
        self.listWidget.show()


    def refreshPieChart(self):

        self.data = db.fetchAppsByDate(today)
        self.chart.createPieChart(self.data)


    def restoreOrMaximizeWindow(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.resize_button.setIcon(QtGui.QIcon(u":/icons/icons/maximize.svg"))
        else:
            self.showMaximized()
            self.ui.resize_button.setIcon(QtGui.QIcon(u":/icons/icons/restore-window.svg"))


    # move window on mouse drag
    def moveWindow(self, e):
        # check if win is maximized
        if self.isMaximized() == False:
            # check if left mouse button is clicked
            if e.buttons() == Qt.LeftButton:
                #move win
                self.move(self.pos() + e.globalPos() - self.clickPosition)
                self.clickPosition = e.globalPos()
                e.accept()


    def mousePressEvent(self, event):
        # current pos of the mouse
        self.clickPosition = event.globalPos()


    # TODO:
    # opening (expanding) and closing the menu
    # def openMenu(self):
    #   width = self.ui.left_menu_fr.width()
    #   print(width)
    #   if width == 50:
    #       newWidth = 200
    #   else:
    #       newWidth = 50

    #   self.ui.left_menu_fr.setMaximumWidth(newWidth)




if __name__ == "__main__":

    data = db.fetchAppsByDate(today)

    app = QApplication(sys.argv)
    window = MainWindow(data)
    window.show()
    sys.exit(app.exec_())
