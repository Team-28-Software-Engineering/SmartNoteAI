import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from notepad import Ui_MainWindow 



class MainScreen(QMainWindow):
	
	def __init__(self):
		super(MainScreen, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		
app = QApplication(sys.argv)
myapp = MainScreen()
myapp.show()
sys.exit(app.exec_())