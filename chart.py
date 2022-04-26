import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
import sqlite3
from datetime import date

from database import *
from ui_gui import *

db = Database()
db.createTable()

today = str(date.today())

data = db.fetchAppsByDate(today)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.setWindowTitle("Time Usage By Application")
        self.setGeometry(100,100, 1280,600)
        self.data = data
        # self.show()

        # self.create_piechart()



    def create_piechart(self):      # ne poziva se
        series = QPieSeries()

        for app in self.data:
            print(app)
            series.append(str(app[1]).title(), app[2])
                
        #adding slice
        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Time Usage By Application")
        
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(chartview)

        self.ui.gridLayout_2.addWidget(chartview, 0, 0, 0, 0)
        # self.ui.stats_body_fr.setStyleSheet(u"background-color: transparent")

        # series.clicked.connect(self.handle_clicked)

        # self.ui.chart_container.setContentsMargins(0, 0, 0, 0)
        # lay = QtWidgets.QHBoxLayout(self.ui.chart_container)
        # lay.setContentsMargins(0, 0, 0, 0)
        # lay.addWidget(chartview)

    # def handle_clicked(self, slice):
    #     print(slice.label(), slice.value())



# App = QApplication(sys.argv)
# window = Window(result)
# sys.exit(App.exec_())