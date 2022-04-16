import sys
import os
from ui_gui import *

import resource_rc

class MainWindow(QMainWindow):
	
	def __init__(self, parent = None):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())