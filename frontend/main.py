import sys
import os
import threading

from bs4 import Stylesheet
from ui_gui import *
from qt_material import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QSizeGrip
from PyQt5.QtCore import Qt

import resource_rc

class MainWindow(QMainWindow):
	
	def __init__(self, parent = None):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		# load stylesheet, overrides fonts set in QTdesigner
		apply_stylesheet(app, theme='light_blue.xml')
		
		# removes window title bar
		self.setWindowFlags(Qt.FramelessWindowHint)

		# sets main background to transparent
		self.setAttribute(Qt.WA_TranslucentBackground)

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



if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())