from ui_gui import *

from PySide2.QtGui import QPainter
from PySide2.QtWidgets import *
from PySide2.QtCharts import QtCharts


class Chart():

    def __init__(self, ui, data):
        self.data = data
        self.ui = ui

        #odabir vrste grafa
        self.series = QtCharts.QPieSeries()
        self.chart = QtCharts.QChart()
        self.chartview = QtCharts.QChartView(self.chart)
        self.lay = QHBoxLayout(self.ui.chart_container)

        self.createPieChart(data)

    def secondsToText(self, secs):
        days = secs//86400
        hours = (secs - days*86400)//3600
        minutes = (secs - days*86400 - hours*3600)//60
        seconds = secs - days*86400 - hours*3600 - minutes*60
        result = ("{} h, ".format(hours) if hours else "") + \
        ("{0:.0f} min, ".format(minutes) if minutes else "") + \
        ("{0:.0f} s ".format(seconds) if seconds else "")
        return result

    def createPieChart(self, data):

        self.data = data

        self.chart.removeSeries(self.series)
        self.series = QtCharts.QPieSeries()

        for app in self.data:
            #print(app)
            self.series.append(str(app[1]).title(), app[2])

        #glavna stvar nakon sto su dodani podaci kreiranje samog grafa
        self.chart.addSeries(self.series)

        #animacije, koje osi se vide sitnice
        self.chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
        self.chart.createDefaultAxes()
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(QtCore.Qt.AlignRight)
        self.chart.legend().setFont(QtGui.QFont("25"))
        self.chart.setBackgroundBrush(QtGui.QBrush("transparent"))

        self.series.setLabelsVisible()
        for slice in self.series.slices():
            slice.setLabelVisible()
            oldLabel = slice.label()
            slice.setLabel(oldLabel + " - " + self.secondsToText(slice.value()))

        #iduce najvaznije prikaz samog grafa
        self.chartview.setRenderHint(QPainter.Antialiasing)
        
        #funkcija koja mi je davala najvise problema koliko kuzim odredivanje bordera
        #prvi parametar sirina grafa po x- osi suzi sa vecim brojevima
        #drugi parametar visina grafa po y- osi smanji sa vecim brojevima
        #treci i cetvrti izgledaju kao da rade istu stvar kao 1. i 2. ne znam 
        self.ui.chart_container.setContentsMargins(0, 0, 0, 0)
                
        #ovo valjda polozi onda graf na kraju na to mjesto
        self.lay.setContentsMargins(0, 0, 0, 0)
        self.lay.addWidget(self.chartview)
        