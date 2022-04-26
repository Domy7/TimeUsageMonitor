import sys
from ui_gui import *

from PySide2.QtGui import QPainter
from PySide2.QtWidgets import *
from PySide2.QtCharts import QtCharts


class Chart():

    def __init__(self, ui, data):
        self.data = data
        self.ui = ui
        self.create_pie_chart()


    def create_pie_chart(self):

        #odabir vrste grafa
        series = QtCharts.QPieSeries()

        #dodavanje podataka
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
        chart.legend().setFont(QtGui.QFont("25"))
        chart.setBackgroundBrush(QtGui.QBrush("transparent"))

        #######################################

        #iduce najvaznije prikaz samog grafa 
        chartview = QtCharts.QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)
        
        #funkcija koja mi je davala najvise problema koliko kuzim odredivanje bordera
        #prvi parametar sirina grafa po x- osi suzi sa vecim brojevima
        #drugi parametar visina grafa po y- osi smanji sa vecim brojevima
        #treci i cetvrti izgledaju kao da rade istu stvar kao 1. i 2. 
        
        self.ui.chart_container.setContentsMargins(0, 0, 0, 0)
         
        #ovo polozi onda graf na kraju na to mjesto
        lay = QHBoxLayout(self.ui.chart_container)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(chartview)

