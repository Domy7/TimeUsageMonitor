import sys, random
from datetime import date

from ui_gui import *

from PySide2.QtWidgets import *
from PySide2.QtCharts import QtCharts
from PySide2.QtGui import QPainter, Qt

from database import *
import calendar
db = Database()

class Bar():

    def __init__(self, ui):
        self.ui = ui

        #odabir vrste grafa
        self.series = QtCharts.QBarSeries()
        self.chart = QtCharts.QChart()
        self.chartview = QtCharts.QChartView(self.chart)
        self.lay = QHBoxLayout(self.ui.weekly_bar_container)

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

        # boja pozadine:
        self.chart.setBackgroundBrush(QtGui.QBrush("transparent"))
        # boja okvira:
        # self.chart.setBackgroundPen(QtGui.QPen(Qt.white))
        # idk:
        # self.chart.setPlotAreaBackgroundPen(QtGui.QPen(Qt.black))
        # self.chart.setPlotAreaBackgroundVisible()

        self.chartview.setRenderHint(QPainter.Antialiasing)
        # self.ui.weekly_bar_container.setContentsMargins(0, 0, 0, 0)
        self.lay.setContentsMargins(0, 0, 0, 0)
        self.lay.addWidget(self.chartview)