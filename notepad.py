# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notepad.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from about import Ui_Dialog 
from PyQt5.QtGui import QKeySequence


class Ui_MainWindow(object):


	def setupUi(self, MainWindow):
		
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(594, 433)
		MainWindow.setWindowIcon(QtGui.QIcon('res/icons/text-editor2.png'))
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
		self.textEdit.setObjectName("textEdit")
		self.horizontalLayout.addWidget(self.textEdit)
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 594, 23))
		self.menubar.setObjectName("menubar")
		self.menuFile = QtWidgets.QMenu(self.menubar)
		self.menuFile.setObjectName("menuFile")
		self.menuEdit = QtWidgets.QMenu(self.menubar)
		self.menuEdit.setObjectName("menuEdit")
		self.menuAbout = QtWidgets.QMenu(self.menubar)
		self.menuAbout.setObjectName("menuAbout")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		self.toolBar = QtWidgets.QToolBar(MainWindow)
		self.toolBar.setObjectName("toolBar")
		MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
		self.actionNew = QtWidgets.QAction(MainWindow)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("res/icons/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionNew.setIcon(icon)
		self.actionNew.setObjectName("actionNew")
		self.actionOpen = QtWidgets.QAction(MainWindow)
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap("res/icons/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionOpen.setIcon(icon1)
		self.actionOpen.setObjectName("actionOpen")
		self.actionSave = QtWidgets.QAction(MainWindow)
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap("res/icons/Save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionSave.setIcon(icon2)
		self.actionSave.setObjectName("actionSave")
		self.actionSave_as = QtWidgets.QAction(MainWindow)
		icon3 = QtGui.QIcon()
		icon3.addPixmap(QtGui.QPixmap("res/icons/Save-as.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionSave_as.setIcon(icon3)
		self.actionSave_as.setObjectName("actionSave_as")
		self.actionCut = QtWidgets.QAction(MainWindow)
		icon4 = QtGui.QIcon()
		icon4.addPixmap(QtGui.QPixmap("res/icons/Cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionCut.setIcon(icon4)
		self.actionCut.setObjectName("actionCut")
		self.actionCopy = QtWidgets.QAction(MainWindow)
		icon5 = QtGui.QIcon()
		icon5.addPixmap(QtGui.QPixmap("res/icons/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionCopy.setIcon(icon5)
		self.actionCopy.setObjectName("actionCopy")
		self.actionPaste = QtWidgets.QAction(MainWindow)
		icon6 = QtGui.QIcon()
		icon6.addPixmap(QtGui.QPixmap("res/icons/Paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionPaste.setIcon(icon6)
		self.actionPaste.setObjectName("actionPaste")
		self.actionRedo = QtWidgets.QAction(MainWindow)
		icon7 = QtGui.QIcon()
		icon7.addPixmap(QtGui.QPixmap("res/icons/Redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionRedo.setIcon(icon7)
		self.actionRedo.setObjectName("actionRedo")
		self.actionUndo = QtWidgets.QAction(MainWindow)
		icon8 = QtGui.QIcon()
		icon8.addPixmap(QtGui.QPixmap("res/icons/Undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionUndo.setIcon(icon8)
		self.actionUndo.setObjectName("actionUndo")
		self.actionAbout_Notepad = QtWidgets.QAction(MainWindow)
		icon9 = QtGui.QIcon()
		icon9.addPixmap(QtGui.QPixmap("res/icons/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionAbout_Notepad.setIcon(icon9)
		self.actionAbout_Notepad.setObjectName("actionAbout_Notepad")
		self.actionExit = QtWidgets.QAction(MainWindow)
		icon10 = QtGui.QIcon()
		icon10.addPixmap(QtGui.QPixmap("res/icons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionExit.setIcon(icon10)
		self.actionExit.setObjectName("actionExit")
		self.menuFile.addAction(self.actionNew)
		self.menuFile.addAction(self.actionOpen)
		self.menuFile.addSeparator()
		self.menuFile.addAction(self.actionSave)
		self.menuFile.addAction(self.actionSave_as)
		self.menuFile.addAction(self.actionExit)
		self.menuEdit.addAction(self.actionCut)
		self.menuEdit.addAction(self.actionCopy)
		self.menuEdit.addAction(self.actionPaste)
		self.menuEdit.addSeparator()
		self.menuEdit.addAction(self.actionRedo)
		self.menuEdit.addAction(self.actionUndo)
		self.menuAbout.addAction(self.actionAbout_Notepad)
		self.menubar.addAction(self.menuFile.menuAction())
		self.menubar.addAction(self.menuEdit.menuAction())
		self.menubar.addAction(self.menuAbout.menuAction())
		self.toolBar.addAction(self.actionNew)
		self.toolBar.addAction(self.actionOpen)
		self.toolBar.addAction(self.actionSave)
		self.toolBar.addAction(self.actionSave_as)
		self.toolBar.addSeparator()
		self.toolBar.addAction(self.actionCut)
		self.toolBar.addAction(self.actionCopy)
		self.toolBar.addAction(self.actionPaste)
		self.toolBar.addSeparator()
		self.toolBar.addAction(self.actionRedo)
		self.toolBar.addAction(self.actionUndo)
		self.toolBar.addSeparator()
		self.toolBar.addAction(self.actionAbout_Notepad)
		self.toolBar.addAction(self.actionExit)

		self.actionNew.setShortcut("Ctrl+N")
		self.actionOpen.setShortcut("Ctrl+O")
		self.actionSave.setShortcut("Ctrl+S")
		self.actionSave_as.setShortcut("Ctrl+Shift+S")
		self.actionCut.setShortcut("Ctrl+X")
		self.actionCopy.setShortcut("Ctrl+C")
		self.actionPaste.setShortcut("Ctrl+V")
		self.actionUndo.setShortcut("Ctrl+Z")
		self.actionRedo.setShortcut("Ctrl+Y")

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Simple Notepad"))
		self.menuFile.setTitle(_translate("MainWindow", "File"))
		self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
		self.menuAbout.setTitle(_translate("MainWindow", "About"))
		self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
		self.actionNew.setText(_translate("MainWindow", "New"))
		self.actionOpen.setText(_translate("MainWindow", "Open"))
		self.actionSave.setText(_translate("MainWindow", "Save"))
		self.actionSave_as.setText(_translate("MainWindow", "Save as"))
		self.actionCut.setText(_translate("MainWindow", "Cut"))
		self.actionCopy.setText(_translate("MainWindow", "Copy"))
		self.actionPaste.setText(_translate("MainWindow", "Paste"))
		self.actionRedo.setText(_translate("MainWindow", "Redo"))
		self.actionUndo.setText(_translate("MainWindow", "Undo"))
		self.actionAbout_Notepad.setText(_translate("MainWindow", "About Notepad"))
		self.actionExit.setText(_translate("MainWindow", "Exit"))

		self.filepath = ''

		self.actionNew.triggered.connect(self.textEdit.clear)
		self.actionOpen.triggered.connect(self.openfile)

		self.actionSave.triggered.connect(self.savefile)
		self.actionSave_as.triggered.connect(self.saveasfile)

		self.actionExit.triggered.connect(self.exitapp)


		self.actionCut.triggered.connect(self.textEdit.cut)
		self.actionCopy.triggered.connect(self.textEdit.copy)
		self.actionPaste.triggered.connect(self.textEdit.paste)

		self.actionUndo.triggered.connect(self.textEdit.undo)
		self.actionRedo.triggered.connect(self.textEdit.redo)


		self.actionAbout_Notepad.triggered.connect(self.aboutapp)

		



	def openfile(self):
		
		filename, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)")

		if filename == "":
			self.textEdit.clear()

		else:
			self.filepath = filename
			f = open(filename, 'r')
			filedata = f.read()
			self.textEdit.setText(filedata)
			f.close()

	

	def savefile(self):

		if not self.filepath:
			filename, _ = QFileDialog.getSaveFileName(None,"QFileDialog.getOpenFileName()", "NewFile","All Files (*);;Python Files (*.py)")
			self.filepath = filename	

		

		else:
			filename = self.filepath
			f = open(filename, 'w')
			filedata = self.textEdit.toPlainText()
			f.write(filedata)
			f.close()


	def saveasfile(self):
		filename, _ = QFileDialog.getSaveFileName(None,"QFileDialog.getOpenFileName()", "NewFile","All Files (*);;Python Files (*.py)")	

		if filename == "":
			pass

		else:
			f = open(filename, 'w')
			filedata = self.textEdit.toPlainText()
			f.write(filedata)
			f.close()

	
	def exitapp(self):
		exit()


	def aboutapp(self):
		# about_text = "Author : Tanzim Rizwan\n"
		# about_text += "Build Date : 12-10-17\n"
		# about_text += "Copyright (C) 2017\n"
		# about_text += "Version : 1.0"
		# QMessageBox.about(None, "ABOUT", about_text)
		
		self.window = QtWidgets.QMainWindow()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self.window)
		self.window.show()


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