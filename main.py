import sys
import os

from bs4 import Stylesheet
from ui_gui import *
from qt_material import *

import resource_rc

###
# from PySide2 import *
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import *
from PySide2.QtCharts import QtCharts
###

import sqlite3
from datetime import date

con = sqlite3.connect('data.db', check_same_thread=False)
cur = con.cursor()

today = str(date.today())

cur.execute('''SELECT * FROM usage WHERE date=?''',(today,))
data = cur.fetchall()

class MainWindow(QMainWindow):
    
    def __init__(self, data, parent = None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.data = data
###
        #poziv funkcije za kreiranje grafa
        self.create_percentage_bar_chart()
###
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
        self.ui.resize_button.clicked.connect(lambda: self.restore_or_maximize_window())

        self.ui.stats_btn.clicked.connect(lambda: self.ui.centralWidget.setCurrentWidget(self.ui.stats_page))
        self.ui.lock_btn.clicked.connect(lambda: self.ui.centralWidget.setCurrentWidget(self.ui.lock_page))
        self.ui.settings_btn.clicked.connect(lambda: self.ui.centralWidget.setCurrentWidget(self.ui.settings_page))
        self.ui.data_btn.clicked.connect(lambda: self.ui.centralWidget.setCurrentWidget(self.ui.data_page))

        # self.ui.header_frame.mouseMoveEvent = self.moveWindow
        self.ui.header_center_fr.mouseMoveEvent = self.moveWindow
        
        # opens menu
        #self.ui.menu_btn.clicked.connect(lambda: self.openMenu())

###
    def create_percentage_bar_chart(self):


        #odabir vrste grafa
        series = QtCharts.QPieSeries()

        for app in self.data:
            print(app)
            series.append(str(app[1]).title(), app[2])

        #glavna stvar nakon sto su dodani podaci kreiranje samog grafa
        chart = QtCharts.QChart()
        chart.addSeries(series)

        #animacije, koje osi se vide sitnice
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
        chart.createDefaultAxes()
        chart.legend().setVisible(True)
        chart.legend().setAlignment(QtCore.Qt.AlignRight)
        background_color = QColor(230, 230, 230)		# postavlja boju pozadine charta da se podudara sa bojom GUI-a, ako je postavljena na 'light_blue.xml' (ln 34)
        chart.setBackgroundBrush(background_color)

        #######################################

        #iduce najvaznije prikaz samog grafa 
        chartview = QtCharts.QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)
        
        #funkcija koja mi je davala najvise problema koliko kuzim odredivanje bordera
        #prvi parametar sirina grafa po x- osi suzi sa vecim brojevima
        #drugi parametar visina grafa po y- osi smanji sa vecim brojevima
        #treci i cetvrti izgledaju kao da rade istu stvar kao 1. i 2. ne znam 
        
        self.ui.chart_container.setContentsMargins(0, 0, 0, 0)
        
        #self.chart_container.setContentsMargins(0, 0, 0, 0) ovako je originalno izgledala funkcija sto meni ne radi mora se dodat self.ui. prije
        
        #ovo valjda polozi onda graf na kraju na to mjesto
        lay = QHBoxLayout(self.ui.chart_container)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(chartview)
###

    def restore_or_maximize_window(self):
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


    # opening (expanding) and closing the menu
    # def openMenu(self):
    # 	width = self.ui.left_menu_fr.width()
    # 	print(width)
    # 	if width == 50:
    # 		newWidth = 200
    # 	else:
    # 		newWidth = 50

    # 	self.ui.left_menu_fr.setMaximumWidth(newWidth)


if __name__ == "__main__":

    

    app = QApplication(sys.argv)
    window = MainWindow(data)
    window.show()
    sys.exit(app.exec_())