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
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QTextEdit, QInputDialog
from PyQt5.QtGui import QIcon, QTextCursor, QTextCharFormat, QColor
from PyQt5.QtCore import Qt



class Ui_MainWindow(object):


	def setupUi(self, MainWindow):
		self.mode = 'light'
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(800, 600)
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
		self.actionSearch = QtWidgets.QAction(MainWindow)
		icon11 = QtGui.QIcon()
		icon11.addPixmap(QtGui.QPixmap("res/icons/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionSearch.setIcon(icon11)
		self.actionSearch.setObjectName("actionSearch")
		self.actionMode = QtWidgets.QAction(MainWindow)
		icon12 = QtGui.QIcon()
		icon12.addPixmap(QtGui.QPixmap("res/icons/mode.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionMode.setIcon(icon12)
		self.actionMode.setObjectName("actionMode")
		self.menuView = QtWidgets.QMenu(self.menubar)
		self.menuView.setObjectName("menuView")
		MainWindow.setMenuBar(self.menubar)
		self.actionBold = QAction(MainWindow)
		self.menuFile.addAction(self.actionNew)
		self.toolBar.addAction(self.actionNew)
		icon13 = QtGui.QIcon()
		icon13.addPixmap(QtGui.QPixmap("res/icons/bold.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionBold.setIcon(icon13)
		self.actionBold.setObjectName("actionBold")
		self.toolBar.addAction(self.actionBold)
		self.actionBold.setCheckable(True)
		self.actionItalic = QAction(MainWindow)
		icon14 = QtGui.QIcon()
		icon14.addPixmap(QtGui.QPixmap("res/icons/italic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionItalic.setIcon(icon14)
		self.actionItalic.setObjectName("actionItalic")
		self.toolBar.addAction(self.actionItalic)
		self.actionItalic.setCheckable(True)
		#################################
		self.actionUnderline = QAction(MainWindow)
		icon15 = QtGui.QIcon()
		icon15.addPixmap(QtGui.QPixmap("res/icons/underline.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionUnderline.setIcon(icon15)
		self.actionUnderline.setObjectName("actionUnderline")
		self.toolBar.addAction(self.actionUnderline)
		self.actionUnderline.setCheckable(True)
		#################################
		self.menuEdit.addAction(self.actionSearch)
		self.toolBar.addAction(self.actionSearch)
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
		self.toolBar.addSeparator()
		spacer = QtWidgets.QWidget()
		spacer.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		self.toolBar.addWidget(spacer)
		self.toolBar.addAction(self.actionExit)
		self.toolBar.addAction(self.actionMode)
		
		

		self.actionNew.setShortcut("Ctrl+N")
		self.actionOpen.setShortcut("Ctrl+O")
		self.actionSave.setShortcut("Ctrl+S")
		self.actionSave_as.setShortcut("Ctrl+Shift+S")
		self.actionCut.setShortcut("Ctrl+X")
		self.actionCopy.setShortcut("Ctrl+C")
		self.actionPaste.setShortcut("Ctrl+V")
		self.actionUndo.setShortcut("Ctrl+Z")
		self.actionRedo.setShortcut("Ctrl+Y")
		self.actionSearch.setShortcut("Ctrl+F")
		self.actionExit.setShortcut("Ctrl+Q")  

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
		self.actionSearch.setText(_translate("MainWindow", "Search"))
		self.actionExit.setText(_translate("MainWindow", "Exit"))

		self.filepath = ''
		self.actionSearch.triggered.connect(self.search_text)
		
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

		self.actionMode.triggered.connect(self.toggle_mode)
		self.actionBold.triggered.connect(self.toggle_bold)
		self.actionItalic.triggered.connect(self.toggle_italic)
		self.actionUnderline.triggered.connect(self.toggle_underline)
		self.actionAbout_Notepad.triggered.connect(self.aboutapp)
		

		
		self.actionMode.setCheckable(True)  # Cho phép nút chuyển đổi giữa hai trạng thái
	def toggle_bold(self):
		if self.actionBold.isChecked():
			self.textEdit.setFontWeight(QtGui.QFont.Bold)
		else:
			self.textEdit.setFontWeight(QtGui.QFont.Normal)
	def toggle_italic(self):
		# Khi tính năng in nghiêng chữ được kích hoạt hoặc tắt
		if self.actionItalic.isChecked():
			self.set_text_italic(True)
		else:
			self.set_text_italic(False)

	def set_text_italic(self, italic):
		# Đặt văn bản in nghiêng hoặc không in nghiêng
		font = self.textEdit.currentFont()
		font.setItalic(italic)
		self.textEdit.setCurrentFont(font)

	def toggle_underline(self):
		# Khi tính năng gạch chân được kích hoạt hoặc tắt
		if self.actionUnderline.isChecked():
			self.set_text_underline(True)
		else:
			self.set_text_underline(False)

	def set_text_underline(self, underline):
		# Đặt văn bản có gạch chân hoặc không có gạch chân
		format = self.textEdit.currentCharFormat()
		format.setFontUnderline(underline)
		self.textEdit.setCurrentCharFormat(format)
	def toggle_mode(self):
		if self.actionMode.isChecked():  # Nếu đang ở chế độ tối
			self.setStyleSheet("background-color: #222; color: #FFF;")
		else:  # Nếu đang ở chế độ sáng
			self.setStyleSheet("")  # Đặt lại stylesheet về mặc định


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
	def remove_highlight(self):
		cursor = self.ui.textEdit.textCursor()
		cursor.clearSelection()
		format = QtGui.QTextCharFormat()
		cursor.setCharFormat(format)

	def search_text(self):
		search_text, ok = QtWidgets.QInputDialog.getText(self.centralwidget, 'Search Text', 'Enter text to search:')
		if ok and search_text:
			cursor = self.textEdit.textCursor()
			cursor.movePosition(QtGui.QTextCursor.Start)
			cursor = self.textEdit.document().find(search_text, cursor)
			if not cursor.isNull():
				self.textEdit.setTextCursor(cursor)
				self.textEdit.ensureCursorVisible()

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

	def toggle_mode(self):
		if self.mode == 'light':
			self.mode = 'dark'
			self.set_dark_mode()
		else:
			self.mode = 'light'
			self.set_light_mode()

	def set_dark_mode(self):
		self.centralwidget.setStyleSheet("background-color: #333; color: #FFF;")
		self.textEdit.setStyleSheet("background-color: #333; color: #FFF;")
		self.menubar.setStyleSheet("background-color: #333; color: #FFF;")
		self.statusbar.setStyleSheet("background-color: #333; color: #FFF;")
		self.toolBar.setStyleSheet("background-color: #333;")
		for action in self.toolBar.actions():
			action.setStyleSheet("color: #FFF;")


	def set_light_mode(self):
		self.centralwidget.setStyleSheet("")
		self.textEdit.setStyleSheet("")
		self.menubar.setStyleSheet("")
		self.statusbar.setStyleSheet("")
		self.toolBar.setStyleSheet("")
		for action in self.toolBar.actions():
			action.setStyleSheet("")


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