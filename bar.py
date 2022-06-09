import sys, random
from datetime import date

from ui_gui import *

from PySide2.QtWidgets import *
# from PyQt5.QtChart import QChart, QChartView, QValueAxis, QBarCategoryAxis, QBarSet, QBarSeries
from PySide2.QtCharts import QtCharts
# from PyQt5.Qt import Qt
from PySide2.QtGui import QPainter

from database import *
import calendar
db = Database()

class Bar():

    def __init__(self, ui):
        # self.data = data
        self.ui = ui

        #odabir vrste grafa
        self.series = QtCharts.QBarSeries()
        self.chart = QtCharts.QChart()
        self.chartview = QtCharts.QChartView(self.chart)
        self.lay = QHBoxLayout(self.ui.weekly_bar_container)

        # self.resize(800, 600)

        self.set0 = QtCharts.QBarSet('Usage in minutes')
        self.maxTime = 0
        self.daysOfWeek = list()
        self.today = date.today()
        for i in range(6, -1, -1):
            day = self.today - timedelta(days=i)
            newDate = str(day.isoformat())
            self.daysOfWeek.append(newDate)
            result = db.getUsageByDate(newDate)
            for day in result:
                if day[0] is None:
                    self.set0.append(0)
                else:
                    mins = round(int(day[0])/60)
                    print(mins)
                    self.set0.append(mins)
                    if mins > self.maxTime:
                        self.maxTime = mins
                       

        self.createBarChart()

    def createBarChart(self):
        self.series.append(self.set0)
        self.chart.addSeries(self.series)
        self.chart.setTitle('Last week usage')
        self.chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        self.axisX = QtCharts.QBarCategoryAxis()
        self.axisX.append(self.daysOfWeek)

        self.axisY = QtCharts.QValueAxis()
        self.axisY.setRange(0, self.maxTime)

        self.chart.addAxis(self.axisX, QtCore.Qt.AlignBottom)
        self.chart.addAxis(self.axisY, QtCore.Qt.AlignLeft)

        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(QtCore.Qt.AlignBottom)

        self.chartview.setRenderHint(QPainter.Antialiasing)
        self.ui.weekly_bar_container.setContentsMargins(0, 0, 0, 0)
        self.lay.setContentsMargins(0, 0, 0, 0)
        self.lay.addWidget(self.chartview)