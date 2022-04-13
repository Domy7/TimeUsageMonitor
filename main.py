import sys
import os
import threading
from ui_gui import *
from vrijeme import *


class MainWindow(QMainWindow):
	
	def __init__(self, parent = None):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)


if __name__ == "__main__":
	time = Vrijeme()
	t1 = threading.Thread(target=time.glavno)
	t1.daemon = True
	t1.start()
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())

