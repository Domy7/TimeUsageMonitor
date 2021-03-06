from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import QHBoxLayout
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

    @staticmethod
    def secondsToText(secs):
        hours = secs // 3600
        minutes = (secs % 3600) // 60
        seconds = (secs % 3600) % 60

        result = ("{} h, ".format(hours) if hours else "") + \
        ("{0:.0f} min, ".format(minutes) if minutes else "") + \
        ("{0:.0f} s, ".format(seconds) if seconds else "")
        result = result[:len(result)-2]
        return result

    def createPieChart(self, data):

        self.data = data

        # za refresh
        self.chart.removeAllSeries()
        self.series = QtCharts.QPieSeries()

        for app in self.data:
            self.series.append(str(app[1]).title(), app[2])

        #glavna stvar nakon sto su dodani podaci kreiranje samog grafa
        self.chart.addSeries(self.series)
        self.chart.setTitle('Today usage')

        #animacije, koje osi se vide sitnice
        self.chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
        self.chart.createDefaultAxes()
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(QtCore.Qt.AlignRight)
        self.chart.legend().setFont(QtGui.QFont("25"))

        # boja pozadine
        self.chart.setBackgroundBrush(QtGui.QBrush("transparent"))

        self.series.setLabelsVisible()
        for slice in self.series.slices():
            slice.setLabelVisible()
            oldLabel = slice.label()
            slice.setLabel(oldLabel + " - " + self.secondsToText(slice.value()))

        #iduce najvaznije prikaz samog grafa
        self.chartview.setRenderHint(QtGui.QPainter.Antialiasing)
        
        #funkcija koja mi je davala najvise problema koliko kuzim odredivanje bordera
        #prvi parametar sirina grafa po x- osi suzi sa vecim brojevima
        #drugi parametar visina grafa po y- osi smanji sa vecim brojevima
        #treci i cetvrti izgledaju kao da rade istu stvar kao 1. i 2. ne znam 
        # self.ui.chart_container.setContentsMargins(0, 0, 0, 0)
                
        #ovo valjda polozi onda graf na kraju na to mjesto
        self.lay.setContentsMargins(0, 0, 0, 0)
        self.lay.addWidget(self.chartview)
        