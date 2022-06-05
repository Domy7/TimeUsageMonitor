import sys, random
from PyQt5.QtWidgets import (QApplication, QMainWindow)
from PyQt5.QtChart import QChart, QChartView, QValueAxis, QBarCategoryAxis, QBarSet, QBarSeries
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPainter

from database import *
import calendar
db = Database()

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.resize(800, 600)

		set0 = QBarSet('Sati')
		maxTime = 0
		daysOfWeek = list()
		today = date.today()
		for i in range(6, -1, -1):
			day = today - timedelta(days=i)
			newDate = str(day.isoformat())
			daysOfWeek.append(newDate)
			result = db.getUsageByDate(newDate)
			for day in result:
				if day[0] is None:
					set0.append(0)
				else:
					set0.append(day[0])
					if day[0] > maxTime: maxTime = day[0]
			
			

			
		

		series = QBarSeries()
		series.append(set0)
	
		chart = QChart()
		chart.addSeries(series)
		chart.setTitle('Last week usage')
		chart.setAnimationOptions(QChart.SeriesAnimations)

		axisX = QBarCategoryAxis()
		axisX.append(daysOfWeek)

		axisY = QValueAxis()
		axisY.setRange(0, maxTime)

		chart.addAxis(axisX, Qt.AlignBottom)
		chart.addAxis(axisY, Qt.AlignLeft)

		chart.legend().setVisible(True)
		chart.legend().setAlignment(Qt.AlignBottom)

		chartView = QChartView(chart)
		self.setCentralWidget(chartView)

if __name__ == '__main__':
	app = QApplication(sys.argv)

	window = MainWindow()
	window.show()

	sys.exit(app.exec_())