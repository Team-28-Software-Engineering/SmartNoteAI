# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notepad.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!
from openai.error import AuthenticationError
from pydub import AudioSegment
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from about import Ui_Dialog 
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QTextEdit, QInputDialog
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtGui import QIcon, QTextCursor, QTextCharFormat, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QTextDocument, QTextImageFormat
from PyQt5.QtGui import QTextImageFormat, QTextCursor, QTextLength
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QDialog, QSlider, QPushButton
from PIL import Image
import pytesseract
import speech_recognition as sr
import enchant
from PyQt5.QtCore import QTimer
import googletrans
from googletrans import Translator
from PyQt5.QtWidgets import QInputDialog, QComboBox
from googletrans import LANGUAGES

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QComboBox, QPushButton, QLabel

class LanguageDialog(QDialog):
    def __init__(self, current_language_code, target_language_code, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Translate Text")
        self.setFixedSize(300, 200)
        self.setWindowIcon(QIcon('res/icons/translate.png'))
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.current_language_code = current_language_code
        self.target_language_code = target_language_code

        layout = QVBoxLayout()

        # Label cho ngôn ngữ hiện tại
        self.current_language_label = QLabel("Current Language:")
        layout.addWidget(self.current_language_label)

        # Combobox cho ngôn ngữ hiện tại
        self.current_language_combo = QComboBox()
        self.current_language_combo.addItem("Auto-detect", "auto")  # Sử dụng "Auto-detect" thay vì "auto"
        for lang_code, lang_name in LANGUAGES.items():
            self.current_language_combo.addItem(lang_name, lang_code)
        self.current_language_combo.setCurrentText("Auto-detect")  # Đặt "Auto-detect" làm giá trị mặc định
        layout.addWidget(self.current_language_combo)

        # Label cho ngôn ngữ muốn dịch sang
        self.target_language_label = QLabel("Translate to:")
        layout.addWidget(self.target_language_label)

        # Combobox cho ngôn ngữ muốn dịch sang
        self.target_language_combo = QComboBox()
        for lang_code, lang_name in LANGUAGES.items():
            self.target_language_combo.addItem(lang_name, lang_code)
        self.target_language_combo.setCurrentText(LANGUAGES[target_language_code])
        layout.addWidget(self.target_language_combo)

        # Nút OK
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)
        layout.addWidget(self.ok_button)

        self.setLayout(layout)

    def get_current_language_code(self):
        return self.current_language_combo.currentData()

    def get_target_language_code(self):
        return self.target_language_combo.currentData()

class InvalidAPIKeyError(Exception):
    pass

class ImageSizeDialog(QDialog):
    def __init__(self, parent=None):
        super(ImageSizeDialog, self).__init__(parent)
        self.setWindowTitle("Resize Image")
        self.setFixedSize(300, 130)
        self.setWindowIcon(QIcon('res/icons/image.png'))
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.layout = QVBoxLayout()

        # Tạo một QLabel để hiển thị kích thước mới của ảnh
        self.size_label = QLabel("Size: 100%")
        self.layout.addWidget(self.size_label)

        # Tạo một QSlider để chọn kích thước mới của ảnh (từ 50% đến 200%)
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(150)
        self.slider.setMaximum(550)
        self.slider.setValue(150)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(25)
        self.slider.valueChanged.connect(self.update_size_label)
        self.layout.addWidget(self.slider)

        # Tạo một nút OK để chấp nhận kích thước mới
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)
        self.layout.addWidget(self.ok_button)

        self.setLayout(self.layout)

    def update_size_label(self):
        size = self.slider.value()
        self.size_label.setText("Size: {}%".format(size))

    def get_size(self):
        return self.slider.value()

class PrintDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Print Settings")
        self.setFixedSize(300, 360)
        self.setWindowIcon(QIcon('res/icons/print.png'))
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        layout = QVBoxLayout()

        # Group box for paper size
        paper_group_box = QGroupBox("Paper Size")
        paper_layout = QVBoxLayout()
        self.paper_combo_box = QComboBox()
        self.paper_combo_box.addItems(["A5", "A6", "A7"])
        paper_layout.addWidget(self.paper_combo_box)
        paper_group_box.setLayout(paper_layout)
        layout.addWidget(paper_group_box)

        # Group box for print orientation
        orientation_group_box = QGroupBox("Orientation")
        orientation_layout = QVBoxLayout()
        self.vertical_radio_button = QRadioButton("Portrait")
        self.horizontal_radio_button = QRadioButton("Landscape")
        orientation_layout.addWidget(self.vertical_radio_button)
        orientation_layout.addWidget(self.horizontal_radio_button)
        orientation_group_box.setLayout(orientation_layout)
        layout.addWidget(orientation_group_box)
         
        # Group box for single or double-sided printing
        sided_group_box = QGroupBox("Sided")
        sided_layout = QVBoxLayout()
        self.single_radio_button = QRadioButton("Single-sided")
        self.double_radio_button = QRadioButton("Double-sided")
        sided_layout.addWidget(self.single_radio_button)
        sided_layout.addWidget(self.double_radio_button)
        sided_group_box.setLayout(sided_layout)
        layout.addWidget(sided_group_box)

        # Print button
        self.print_button = QPushButton("Print")
        layout.addWidget(self.print_button)

        self.setLayout(layout)

class ApiKeyInputDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enter API Key")
        self.setWindowIcon(QIcon('res/icons/gpt.png'))
        self.setFixedSize(300, 150)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.label = QLabel("Please enter your OpenAI API Key:")
        self.input_field = QLineEdit()
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_api_key)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.submit_button)
        self.setLayout(layout)

    def submit_api_key(self):
        api_key = self.input_field.text().strip()
        if api_key:
            config.API_KEY = api_key
            self.accept()


class Ui_MainWindow(object):


	def setupUi(self, MainWindow):
		self.previous_api_keys = []
		self.current_language_code = "auto"  # Giá trị mặc định cho ngôn ngữ hiện tại
		self.target_language_code = "en" 
		self.currentFontColor = QtGui.QColor(QtCore.Qt.black)
		self.currentHighlightColor = QtGui.QColor(QtCore.Qt.yellow)
		self.word_count_checked = True
		self.char_count_checked = True
		self.line_count_checked = True
		self.show_font_checked = False
		self.spell_check_checked = True
		self.mode = 'light'
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(1200, 800)
		MainWindow.setWindowIcon(QtGui.QIcon('res/icons/notepad.png'))
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
	
		self.actionBold.setCheckable(True)
		self.actionItalic = QAction(MainWindow)
		icon14 = QtGui.QIcon()
		icon14.addPixmap(QtGui.QPixmap("res/icons/italic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionItalic.setIcon(icon14)
		self.actionItalic.setObjectName("actionItalic")
		self.actionItalic.setCheckable(True)
		self.actionUnderline = QAction(MainWindow)
		icon15 = QtGui.QIcon()
		icon15.addPixmap(QtGui.QPixmap("res/icons/underline.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionUnderline.setIcon(icon15)
		self.actionUnderline.setObjectName("actionUnderline")
		self.actionUnderline.setCheckable(True)
		self.actionStatistics = QtWidgets.QAction(MainWindow)
		icon16 = QtGui.QIcon()
		icon16.addPixmap(QtGui.QPixmap("res/icons/stat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionStatistics.setIcon(icon16)
		self.actionStatistics.setObjectName("actionStatistics")
		#########################
		self.actionTranslate = QAction(MainWindow)
		icon_translate = QtGui.QIcon()
		icon_translate.addPixmap(QtGui.QPixmap("res/icons/translate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionTranslate.setIcon(icon_translate)
		self.actionTranslate.setObjectName("actionTranslate")
		#########################
		self.actionInsertImage = QtWidgets.QAction(MainWindow)
		icon18 = QtGui.QIcon()
		icon18.addPixmap(QtGui.QPixmap("res/icons/image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionInsertImage.setIcon(icon18)
		self.actionInsertImage.setObjectName("actionInsertImage")
		self.actionFont = QAction(MainWindow)
		self.actionFont.setObjectName("actionFont")
		icon19 = QtGui.QIcon()
		icon19.addPixmap(QtGui.QPixmap("res/icons/font.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionFont.setIcon(icon19)
		self.actionFont.setObjectName("actionFont") 
		self.actionOCR = QtWidgets.QAction(MainWindow)
		icon20 = QtGui.QIcon()
		icon20.addPixmap(QtGui.QPixmap("res/icons/ocr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionOCR.setIcon(icon20)
		self.actionOCR.setObjectName("actionOCR")
		self.chat_action = QtWidgets.QAction(MainWindow)
		icon21 = QtGui.QIcon()
		icon21.addPixmap(QtGui.QPixmap("res/icons/gpt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.chat_action.setIcon(icon21)
		#################################
		self.actionAudio_to_Text = QtWidgets.QAction(MainWindow)
		icon22 = QtGui.QIcon()
		icon22.addPixmap(QtGui.QPixmap("res/icons/audio2text.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionAudio_to_Text.setIcon(icon22)
		self.actionAudio_to_Text.setObjectName("actionAudio_to_Text")
		#################################
		#################################
		self.actionFontColor = QtWidgets.QAction(MainWindow)
		icon_fontcolor = QtGui.QIcon()
		icon_fontcolor.addPixmap(QtGui.QPixmap("res/icons/fontcolor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionFontColor.setIcon(icon_fontcolor)
		self.actionFontColor.setObjectName("actionFontColor")
		self.actionPrint = QtWidgets.QAction(MainWindow)
		icon_print = QtGui.QIcon()
		icon_print.addPixmap(QtGui.QPixmap("res/icons/print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionPrint.setIcon(icon_print)
		self.actionPrint.setObjectName("actionPrint")
		self.actionHighlight = QtWidgets.QAction(MainWindow)
		icon_highlight = QtGui.QIcon()
		icon_highlight.addPixmap(QtGui.QPixmap("res/icons/highlight.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionHighlight.setIcon(icon_highlight)
		self.actionHighlight.setObjectName("actionHighlight")
		#################################
		self.toolBar.addAction(self.actionFontColor)
		self.toolBar.addAction(self.actionHighlight)
		self.toolBar.addAction(self.actionFont)
		self.toolBar.addAction(self.actionBold)
		self.toolBar.addAction(self.actionItalic)
		self.toolBar.addAction(self.actionUnderline)
		self.toolBar.addAction(self.actionInsertImage)
		self.toolBar.addSeparator()
		self.toolBar.addAction(self.actionTranslate)
		self.toolBar.addAction(self.chat_action)
		self.toolBar.addAction(self.actionOCR)
		self.toolBar.addAction(self.actionAudio_to_Text)
		self.toolBar.addSeparator()
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
		self.toolBar.addAction(self.actionStatistics)
		self.toolBar.addSeparator()
		self.toolBar.addAction(self.actionExit)
		self.toolBar.addAction(self.actionMode)
		
		

		self.actionNew.setShortcut("Ctrl+N")
		self.actionOpen.setShortcut("Ctrl+O")
		self.actionSave.setShortcut("Ctrl+S")
		self.actionSave_as.setShortcut("Ctrl+Shift+S")
		self.actionPrint.setShortcut("Ctrl+P")
		self.actionCut.setShortcut("Ctrl+X")
		self.actionCopy.setShortcut("Ctrl+C")
		self.actionPaste.setShortcut("Ctrl+V")
		self.actionBold.setShortcut("Ctrl+B")
		self.actionItalic.setShortcut("Ctrl+I")
		self.actionUnderline.setShortcut("Ctrl+U")
		self.actionTranslate.setShortcut("Ctrl+T")
		self.actionUndo.setShortcut("Ctrl+Z")
		self.actionRedo.setShortcut("Ctrl+Y")
		self.actionSearch.setShortcut("Ctrl+F")
		self.actionExit.setShortcut("Ctrl+Q")  

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		#########
		self.textEdit.textChanged.connect(self.update_statistics)
		self.wordCountLabel = QtWidgets.QLabel("Words: 0")
		self.characterCountLabel = QtWidgets.QLabel("Characters: 0")
		self.lineCountLabel = QtWidgets.QLabel("Lines: 0")

		MainWindow.statusBar().addPermanentWidget(self.wordCountLabel)
		MainWindow.statusBar().addPermanentWidget(self.characterCountLabel)
		MainWindow.statusBar().addPermanentWidget(self.lineCountLabel)
		#########
		self.textEdit.setAcceptDrops(True)
		self.textEdit.dragEnterEvent = self.drag_enter_event
		self.textEdit.dropEvent = self.drop_event
		#########
		openai.api_key = config.API_KEY
		self.chatbot_frame = QWidget(self.centralwidget)
		self.chat_input = QLineEdit(self.chatbot_frame)
		self.chat_button = QPushButton("Send", self.chatbot_frame)

		# Tạo layout chính cho cửa sổ
		vbox_main = QVBoxLayout()
		vbox_main.addWidget(self.textEdit)

		# Tạo layout cho khung chat và nút gửi tin nhắn, nhưng ẩn nó ban đầu
		self.chatbot_frame.hide()
		hbox_chat = QHBoxLayout()
		hbox_chat.addWidget(self.chat_input)
		hbox_chat.addWidget(self.chat_button)
		self.chatbot_frame.setLayout(hbox_chat)
		vbox_main.addWidget(self.chatbot_frame)

		self.horizontalLayout.addLayout(vbox_main)

		# Kết nối sự kiện clicked của nút gửi tin nhắn
		self.chat_button.clicked.connect(self.send_message)

		# Kết nối sự kiện enter của QLineEdit để gửi tin nhắn
		self.chat_input.returnPressed.connect(self.send_message)
		#########
		# Khởi tạo enchant dictionary
		self.spell_checker = enchant.Dict("en_US")

		# Tạo một QTimer để kiểm tra lỗi chính tả sau một khoảng thời gian chờ
		self.spell_check_timer = QTimer()
		self.spell_check_timer.timeout.connect(self.check_spelling)

		# Kết nối sự kiện văn bản thay đổi để bắt đầu kiểm tra chính tả
		self.textEdit.textChanged.connect(self.start_spell_check_timer)
		#########
		
		#########

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "SmartNoteAI"))
		self.menuFile.setTitle(_translate("MainWindow", "File"))
		self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
		self.menuAbout.setTitle(_translate("MainWindow", "About"))
		self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
		self.actionNew.setText(_translate("MainWindow", "New"))
		self.actionOpen.setText(_translate("MainWindow", "Open"))
		self.actionSave.setText(_translate("MainWindow", "Save"))
		self.actionSave_as.setText(_translate("MainWindow", "Save as"))
		self.actionPrint.setText(_translate("MainWindow", "Print"))
		self.actionCut.setText(_translate("MainWindow", "Cut"))
		self.actionCopy.setText(_translate("MainWindow", "Copy"))
		self.actionPaste.setText(_translate("MainWindow", "Paste"))
		self.actionRedo.setText(_translate("MainWindow", "Redo"))
		self.actionUndo.setText(_translate("MainWindow", "Undo"))
		self.actionAbout_Notepad.setText(_translate("MainWindow", "About Notepad"))
		self.actionSearch.setText(_translate("MainWindow", "Search"))
		self.actionStatistics.setText(_translate("MainWindow", "Display"))
		self.actionExit.setText(_translate("MainWindow", "Exit"))
		self.actionFontColor.setText(_translate("MainWindow", "Font Color"))
		self.actionFont.setText(_translate("MainWindow", "Font"))
		self.actionBold.setText(_translate("MainWindow", "Bold"))
		self.actionItalic.setText(_translate("MainWindow", "Italic"))
		self.actionUnderline.setText(_translate("MainWindow", "Underline"))
		self.actionInsertImage.setText(_translate("MainWindow", "Insert Image"))
		self.actionTranslate.setText(_translate("MainWindow", "Translate"))
		self.chat_action.setText(_translate("MainWindow", "Chatbot"))
		self.actionOCR.setText(_translate("MainWindow", "Image to Text"))
		self.actionAudio_to_Text.setText(_translate("MainWindow", "Audio to Text"))
		self.actionHighlight.setText(_translate("MainWindow", "Highlight"))
		self.actionMode.setText(_translate("MainWindow", "Mode"))

		self.filepath = ''
		self.actionSearch.triggered.connect(self.search_text)
		
		self.actionOpen.triggered.connect(self.openfile)

		self.actionSave.triggered.connect(self.savefile)
		self.actionSave_as.triggered.connect(self.saveasfile)

		self.actionExit.triggered.connect(self.exitapp)


		self.actionCut.triggered.connect(self.textEdit.cut)
		self.actionCopy.triggered.connect(self.textEdit.copy)
		self.actionPaste.triggered.connect(self.textEdit.paste)
		self.actionPrint.triggered.connect(self.print_document)

		self.actionUndo.triggered.connect(self.textEdit.undo)
		self.actionRedo.triggered.connect(self.textEdit.redo)

		self.actionMode.triggered.connect(self.toggle_mode)
		self.actionBold.triggered.connect(self.toggle_bold)
		self.actionItalic.triggered.connect(self.toggle_italic)
		self.actionUnderline.triggered.connect(self.toggle_underline)
		self.actionAbout_Notepad.triggered.connect(self.aboutapp)
		self.actionStatistics.triggered.connect(self.show_statistics_dialog)
		self.actionInsertImage.triggered.connect(self.insert_image)
		self.actionFont.triggered.connect(self.choose_font)
		self.actionOCR.triggered.connect(self.perform_ocr)
		self.chat_action.triggered.connect(self.toggle_chat)
		self.actionAudio_to_Text.triggered.connect(self.audio_to_text)
		self.actionFontColor.triggered.connect(self.fontColor)
		self.actionHighlight.triggered.connect(self.highlight)
		self.actionTranslate.triggered.connect(self.translate_text)

		
		self.actionMode.setCheckable(True)  # Cho phép nút chuyển đổi giữa hai trạng thái

	def toggle_chat(self):
        # Kiểm tra xem chatbot đã mở hay không
		if self.chatbot_frame.isVisible():
			# Nếu chatbot đang mở, ẩn nó đi và không thực hiện thay đổi API
			self.chatbot_frame.setVisible(False)
		else:
			# Kiểm tra xem API đã được cung cấp trong cấu hình hay không
			if config.API_KEY:
				# Nếu có API, hỏi người dùng có muốn thay đổi không
				reply = QMessageBox.question(self.centralwidget, 'API Confirmation', 
												'Do you want to change your API key?', 
												QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
				if reply == QMessageBox.Yes:
					# Nếu người dùng muốn thay đổi, hiển thị cửa sổ nhập API
					api_key, ok = QInputDialog.getItem(self.centralwidget, 'Enter API Key', 
														'Enter your API key:', self.previous_api_keys, editable=True)
					if ok:
						config.API_KEY = api_key
						if api_key not in self.previous_api_keys:
							self.previous_api_keys.append(api_key)
			else:
				# Nếu không có API, yêu cầu người dùng nhập API key
				api_key, ok = QInputDialog.getItem(self.centralwidget, 'Enter API Key', 
													'Enter your API key:', self.previous_api_keys, editable=True)
				if ok:
					config.API_KEY = api_key
					if api_key not in self.previous_api_keys:
						self.previous_api_keys.append(api_key)

				# Kiểm tra lại xem có API key hay không
				if not config.API_KEY:
					# Nếu không có API key, ẩn thanh chat
					self.chatbot_frame.setVisible(False)
					return

			# Hiển thị hoặc ẩn khung chat khi nút chat được nhấn
			self.chatbot_frame.setVisible(not self.chatbot_frame.isVisible())

	def request_api_key(self):
		# Hiển thị hộp thoại yêu cầu nhập API key
		api_key, ok = QInputDialog.getText(self.centralwidget, 'Enter API Key', 
											'Enter your API key:')
		if ok:
			# Kiểm tra tính hợp lệ của API key
			try:
				self.validate_api_key(api_key)
				config.API_KEY = api_key
				# Thêm API key vào danh sách các API đã nhập đúng
				self.valid_api_keys.append(api_key)
			except InvalidAPIKeyError as e:
				QMessageBox.warning(self.centralwidget, 'Invalid API Key', str(e))
				# Nếu API không hợp lệ, yêu cầu nhập lại
				self.request_api_key()

	def show_api_content(self):
		if config.API_KEY:
			QMessageBox.information(self.centralwidget, 'API Key Content', 
									f'Your API key is: {config.API_KEY}', QMessageBox.Ok)
		else:
			QMessageBox.warning(self.centralwidget, 'API Key Content', 
									'No API key is currently set.', QMessageBox.Ok)

	def show_api_key_dialog(self):
		dialog = ApiKeyInputDialog()
		if dialog.exec_() == QDialog.Accepted:
			QMessageBox.information(self.centralwidget, "Success", "API Key has been saved. You can now use the chatbot.")

	def setup_chatbot_frame(self):
		self.chatbot_frame = QWidget(self.centralwidget)
		self.chat_input = QLineEdit(self.chatbot_frame)
		self.chat_button = QPushButton("Send", self.chatbot_frame)
		self.api_info_button = QPushButton("API Info", self.chatbot_frame)  # Nút mới

		# Tạo layout chính cho cửa sổ
		vbox_main = QVBoxLayout()
		vbox_main.addWidget(self.textEdit)

		# Tạo layout cho khung chat và nút gửi tin nhắn, nhưng ẩn nó ban đầu
		self.chatbot_frame.hide()
		hbox_chat = QHBoxLayout()
		hbox_chat.addWidget(self.chat_input)
		hbox_chat.addWidget(self.chat_button)
		hbox_chat.addWidget(self.api_info_button)  # Thêm nút mới vào layout
		self.chatbot_frame.setLayout(hbox_chat)
		vbox_main.addWidget(self.chatbot_frame)

		self.horizontalLayout.addLayout(vbox_main)

		# Kết nối sự kiện clicked của nút gửi tin nhắn
		self.chat_button.clicked.connect(self.send_message)

		# Kết nối sự kiện clicked của nút thông tin API
		self.api_info_button.clicked.connect(self.show_api_content)

		# Kết nối sự kiện enter của QLineEdit để gửi tin nhắn
		self.chat_input.returnPressed.connect(self.send_message)

	def send_message(self):
		user_input = self.chat_input.text().strip()
		if user_input:
			try:
				response = openai.ChatCompletion.create(
					model="gpt-3.5-turbo-0125",
					messages=[
						{"role": "system", "content": "You are a helpful assistant."},
						{"role": "user", "content": user_input}
					],
					max_tokens=1000,
					api_key=config.API_KEY  # Sử dụng API từ cấu hình
				)
				text = response.choices[0].message["content"]
				self.textEdit.append(f"\nUser: {user_input}\nChatbot: {text}\n")
				self.chat_input.clear()
			except AuthenticationError as e:
				# Hiển thị cảnh báo lỗi
				QMessageBox.warning(self.centralwidget, 'Authentication Error', str(e))
				# Yêu cầu nhập API mới
				api_key, ok = QInputDialog.getItem(self.centralwidget, 'Enter API Key', 
													'Enter your API key:', self.previous_api_keys, editable=True)
				if ok:
					config.API_KEY = api_key
					if api_key not in self.previous_api_keys:
						self.previous_api_keys.append(api_key)
					# Thử lại gửi tin nhắn
					self.send_message()
			except Exception as e:
				# Xử lý các loại lỗi khác nếu cần
				QMessageBox.warning(self.centralwidget, 'Error', str(e))
				
	def fontColor(self):
		color = QtWidgets.QColorDialog.getColor(self.currentFontColor)
		if color.isValid():
			self.currentFontColor = color
			self.textEdit.setTextColor(color)

	def highlight(self):
		color = QtWidgets.QColorDialog.getColor(self.currentHighlightColor)
		if color.isValid():
			self.currentHighlightColor = color
			self.textEdit.setTextBackgroundColor(color)

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
		
		filename, _ = QFileDialog.getOpenFileName(None,"Open File", "","All Files (*);;Python Files (*.py)")

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
			filename, _ = QFileDialog.getSaveFileName(
				None,
				"Save File",
				"NewFile.txt",  # Tên file mặc định là NewFile.txt
				"Text Files (*.txt);;Word Documents (*.doc *.docx);;Markdown Files (*.md);;JSON Files (*.json);;All Files (*)"
			)
			if filename:  # Kiểm tra xem filename có tồn tại không
				self.filepath = filename
			else:
				return  # Nếu người dùng hủy, thoát khỏi hàm mà không làm gì thêm

		filename = self.filepath

		# Lưu nội dung vào file
		try:
			with open(filename, 'w', encoding='utf-8') as f:
				filedata = self.textEdit.toPlainText()
				f.write(filedata)
		except Exception as e:
			print(f"Error saving file: {e}")

	def saveasfile(self):
		filename, _ = QFileDialog.getSaveFileName(
			None,
			"Save As File",
			"NewFile.txt",  # Tên file mặc định là NewFile.txt
			"Text Files (*.txt);;Word Documents (*.doc *.docx);;Markdown Files (*.md);;JSON Files (*.json);;All Files (*)"
		)
		
		if filename:
			try:
				with open(filename, 'w', encoding='utf-8') as f:
					filedata = self.textEdit.toPlainText()
					f.write(filedata)
				self.filepath = filename  # Cập nhật filepath mới sau khi lưu thành công
			except Exception as e:
				print(f"Error saving file: {e}")
		else:
			return  # Nếu người dùng hủy, thoát khỏi hàm mà không làm gì thêm

	def print_document(self):
		print_dialog = PrintDialog()  
		print_dialog.exec_()
		
	def exitapp(self):
		reply = QMessageBox.question(None, 'Message', 'Do you want to save the file before exiting?', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)

		if reply == QMessageBox.Yes:
			self.savefile()
			exit()
		elif reply == QMessageBox.No:
			exit()
		else:
			pass


	def aboutapp(self):
		# about_text = "Author : Team-28-Software-Engineering\n"
		# about_text += "Build Date : 15/5/2024\n"
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
		self.menubar.setStyleSheet("background-color: #666; color: #FFF;")  # Đảo màu nền và màu chữ
		self.statusbar.setStyleSheet("background-color: #333; color: #FFF;")
		self.toolBar.setStyleSheet("background-color: #666; color: #FFF;")
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

	def update_statistics(self):
		# Lấy văn bản từ QTextEdit
		text = self.textEdit.toPlainText()

		# Thống kê số từ, ký tự và dòng
		word_count = len(text.split())
		character_count = len(text)
		line_count = text.count('\n') + 1

		# Hiển thị thông tin thống kê trên thanh trạng thái
		self.wordCountLabel.setText("Words: " + str(word_count))
		self.characterCountLabel.setText("Characters: " + str(character_count))
		self.lineCountLabel.setText("Lines: " + str(line_count))

	def show_statistics_dialog(self):
		dialog = QtWidgets.QDialog()
		dialog.setWindowTitle("Display Options")
		dialog.setWindowIcon(QIcon('res/icons/notepad.png'))
		dialog.setFixedSize(260, 300)
		dialog.setWindowFlags(dialog.windowFlags() & ~Qt.WindowContextHelpButtonHint)

		layout = QtWidgets.QVBoxLayout()

		word_count_check = QtWidgets.QCheckBox("Word Count")
		char_count_check = QtWidgets.QCheckBox("Character Count")
		line_count_check = QtWidgets.QCheckBox("Line Count")
		font_check = QtWidgets.QCheckBox("Show Current Font")
		spell_check_check = QtWidgets.QCheckBox("Check Spelling")

		# Thiết lập trạng thái ban đầu của các checkbox
		word_count_check.setChecked(self.word_count_checked)
		char_count_check.setChecked(self.char_count_checked)
		line_count_check.setChecked(self.line_count_checked)
		font_check.setChecked(self.show_font_checked)
		spell_check_check.setChecked(self.spell_check_checked)

		layout.addWidget(word_count_check)
		layout.addWidget(char_count_check)
		layout.addWidget(line_count_check)
		layout.addWidget(font_check)
		layout.addWidget(spell_check_check)

		button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
		button_box.accepted.connect(dialog.accept)
		button_box.rejected.connect(dialog.reject)

		layout.addWidget(button_box)

		dialog.setLayout(layout)

		if dialog.exec_():
			# Lưu lại trạng thái của các checkbox
			self.word_count_checked = word_count_check.isChecked()
			self.char_count_checked = char_count_check.isChecked()
			self.line_count_checked = line_count_check.isChecked()
			self.show_font_checked = font_check.isChecked()
			self.spell_check_checked = spell_check_check.isChecked()

			# Hiển thị hoặc ẩn các phần thống kê tương ứng
			if self.word_count_checked:
				self.wordCountLabel.show()
			else:
				self.wordCountLabel.hide()

			if self.char_count_checked:
				self.characterCountLabel.show()
			else:
				self.characterCountLabel.hide()

			if self.line_count_checked:
				self.lineCountLabel.show()
			else:
				self.lineCountLabel.hide()

			# Hiển thị hoặc ẩn tên font hiện tại
			if self.show_font_checked:
				self.show_current_font(self.textEdit.currentFont())
			else:
				existing_widget = self.statusbar.findChild(QtWidgets.QLabel, "fontLabel")
				if existing_widget:
					existing_widget.deleteLater()

			# Bật hoặc tắt kiểm tra chính tả
			if self.spell_check_checked:
				self.start_spell_check_timer()
			else:
				self.stop_spell_check_timer()
				# Set text color to black when spell check is disabled
				self.set_text_color(Qt.black)

	def set_text_color(self, color):
		cursor = self.textEdit.textCursor()
		cursor.select(QtGui.QTextCursor.Document)

		# Lặp qua từng ký tự trong văn bản
		for pos in range(cursor.selectionStart(), cursor.selectionEnd()):
			cursor.setPosition(pos)
			cursor.movePosition(QtGui.QTextCursor.Right, QtGui.QTextCursor.KeepAnchor, 1)
			
			# Lấy format của ký tự hiện tại
			char_format = cursor.charFormat()
			
			# Kiểm tra trạng thái của hộp kiểm "Check Spelling"
			spelling_enabled = self.spell_check_checked

			# Nếu kiểm tra chính tả đang được bật, áp dụng gạch chân nhiễu
			if spelling_enabled:
				char_format.setUnderlineStyle(QtGui.QTextCharFormat.SpellCheckUnderline)
			else:
				# Nếu kiểm tra chính tả được tắt, loại bỏ gạch chân nhiễu
				char_format.setUnderlineStyle(QtGui.QTextCharFormat.NoUnderline)

			# Áp dụng lại format cho ký tự
			cursor.setCharFormat(char_format)

	def show_current_font(self, font):
		# Kiểm tra xem checkbox "Show Current Font" đã được chọn hay không
		if not self.show_font_checked:
			return  # Không hiển thị thông tin font nếu checkbox chưa được chọn

		# Nếu font hiện tại là None, gán font là "Arial"
		if font is None:
			font = QtGui.QFont("Arial")

		# Hiển thị tên font hiện tại ở góc trái notepad
		font_info = "Current Font: " + font.family()

		# Kiểm tra xem đã có một widget hiển thị tên font trước đó hay chưa
		existing_widget = self.statusbar.findChild(QtWidgets.QLabel, "fontLabel")

		if existing_widget:  # Nếu đã tồn tại widget
			# Cập nhật nội dung của widget
			existing_widget.setText(font_info)
		else:
			# Tạo một QLabel mới và hiển thị tên font
			font_label = QtWidgets.QLabel(font_info)
			font_label.setObjectName("fontLabel")  # Đặt tên cho widget để có thể tìm lại sau này
			self.statusbar.insertWidget(0, font_label)
			
	def hide_current_font(self):
		# Tìm và xóa widget hiển thị tên font hiện tại
		font_label = self.statusbar.findChild(QtWidgets.QLabel, "fontLabel")
		if font_label:
			font_label.deleteLater()

	def insert_image(self):
		# Mở hộp thoại để chọn tệp ảnh
		filename, _ = QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *.bmp *.gif)")

		# Kiểm tra nếu người dùng đã chọn tệp
		if filename:
			# Hiển thị hộp thoại để chọn kích thước ảnh
			size_dialog = ImageSizeDialog()
			if size_dialog.exec_():
				size = size_dialog.get_size()

				# Tạo đối tượng QTextImageFormat từ tệp ảnh và kích thước
				image_format = QTextImageFormat()
				image_format.setName(filename)
				image_format.setWidth(size)

				# Chèn ảnh vào vị trí hiện tại của con trỏ
				cursor = self.textEdit.textCursor()
				cursor.insertImage(image_format)

	def drag_enter_event(self, event):
		if event.mimeData().hasUrls():
			event.acceptProposedAction()

	def drop_event(self, event):
		mime_data = event.mimeData()
		if mime_data.hasUrls():
			urls = mime_data.urls()
			for url in urls:
				if url.isLocalFile():
					file_path = url.toLocalFile()
					if file_path.lower().endswith(('.png', '.jpg', '.bmp', '.gif')):
						self.insert_image(file_path)

	def choose_font(self):
		# Hiển thị hộp thoại chọn font
		font, ok = QFontDialog.getFont()
		if ok:
			# Lấy font mới từ hộp thoại và thiết lập font cho textEdit
			self.textEdit.setCurrentFont(font)

			# Hiển thị tên font hiện tại ở góc trái notepad
			self.show_current_font(font)

	def perform_ocr(self):
		# Open a file dialog to select an image
		filename, _ = QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *.bmp *.gif)")
		
		# Check if a file was selected
		if filename:
			# Use Pillow to open the image
			image = Image.open(filename)
			
			# Use pytesseract to perform OCR on the image and extract text
			extracted_text = pytesseract.image_to_string(image)
			
			# Append the extracted text to the text edit
			self.textEdit.append(extracted_text)

	def audio_to_text(self):
		# Mở cửa sổ để chọn file âm thanh
		filename, _ = QFileDialog.getOpenFileName(None, "Select Audio File", "", "Audio Files (*.wav *.mp3)")

		if filename == "":
			return

		try:
			# Chuyển đổi file mp3 thành WAV để nhận dạng âm thanh
			sound = AudioSegment.from_mp3(filename)
			filename_wav = filename[:-4] + ".wav"
			sound.export(filename_wav, format="wav")

			# Sử dụng thư viện SpeechRecognition để nhận dạng âm thanh
			recognizer = sr.Recognizer()
			with sr.AudioFile(filename_wav) as source:
				audio_data = recognizer.record(source)
				text = recognizer.recognize_google(audio_data)

			# Thêm văn bản nhận dạng được vào cuối textEdit
			self.textEdit.moveCursor(QtGui.QTextCursor.End)
			self.textEdit.insertPlainText(text)

		except Exception as e:
			# Nếu có lỗi, thông báo cho người dùng
			QMessageBox.warning(None, "Error", str(e))

	def start_spell_check_timer(self):
		if self.spell_check_checked:
			self.spell_check_timer.start(1000) 

	def stop_spell_check_timer(self):
		self.spell_check_timer.stop() 

	def check_spelling(self):
		self.spell_check_timer.stop()  # Dừng bộ đếm thời gian
		cursor = self.textEdit.textCursor()
		cursor_pos = cursor.position()  # Lưu lại vị trí của con trỏ

		# Lấy văn bản trong textEdit
		text = self.textEdit.toPlainText()

		# Tạo một danh sách để lưu trữ màu chữ của từng phần văn bản
		char_formats = []

		# Tách văn bản thành các từ và kiểm tra chính tả
		for start_pos, end_pos, word in self.iterate_words(text):
			if not self.spell_checker.check(word):
				# Nếu từ không đúng chính tả, lưu màu chữ hiện tại và áp dụng gạch chân nhiễu
				cursor.setPosition(start_pos)
				cursor.movePosition(QtGui.QTextCursor.Right, QtGui.QTextCursor.KeepAnchor, end_pos - start_pos)
				char_format = cursor.charFormat()
				char_formats.append((start_pos, char_format.foreground()))  # Lưu trữ màu chữ hiện tại
				char_format.setUnderlineStyle(QtGui.QTextCharFormat.SpellCheckUnderline)
				char_format.setUnderlineColor(Qt.red)  # Đặt màu gạch chân nhiễu là màu đỏ
				cursor.setCharFormat(char_format)
			else:
				char_formats.append(None)  # Không áp dụng gạch chân nhiễu, để màu chữ không thay đổi

		# Khôi phục màu chữ ban đầu cho các từ không cần áp dụng gạch chân nhiễu
		for i, char_format in enumerate(char_formats):
			if char_format is None:
				continue
			start_pos, color = char_format
			cursor.setPosition(start_pos)
			cursor.movePosition(QtGui.QTextCursor.Right, QtGui.QTextCursor.KeepAnchor, 1)
			char_format = cursor.charFormat()
			char_format.setForeground(color)  # Thiết lập màu chữ trở lại
			cursor.setCharFormat(char_format)

		# Khôi phục vị trí của con trỏ
		cursor.setPosition(cursor_pos)



	def iterate_words(self, text):
		"""
		Hàm này tách văn bản thành các từ và trả về vị trí bắt đầu và kết thúc của từ trong văn bản cùng với từ đó.
		"""
		in_word = False
		start_pos = 0
		for pos, char in enumerate(text):
			if char.isalnum():
				if not in_word:
					start_pos = pos
					in_word = True
			else:
				if in_word:
					yield start_pos, pos, text[start_pos:pos]
					in_word = False
		if in_word:
			yield start_pos, len(text), text[start_pos:]
			
	def translate_text(self):
		dialog = LanguageDialog(self.current_language_code, self.target_language_code)
		
		if dialog.exec_() == QDialog.Accepted:
			self.current_language_code = dialog.get_current_language_code()
			self.target_language_code = dialog.get_target_language_code()
			translator = Translator()
			current_text = self.textEdit.toPlainText()
			translated_text = translator.translate(current_text, src=self.current_language_code, dest=self.target_language_code).text
			self.textEdit.setText(translated_text)
	













import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from notepad import Ui_MainWindow 
import openai
import config

class MainScreen(QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.textEdit.setAcceptDrops(True)
        self.ui.textEdit.dragEnterEvent = self.drag_enter_event
        self.ui.textEdit.dropEvent = self.drop_event
        self.ui.actionNew.triggered.connect(self.new_notepad)

    def new_notepad(self):
        new_notepad = MainScreen()
        new_notepad.show()

    def drag_enter_event(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def drop_event(self, event):
        mime_data = event.mimeData()
        if mime_data.hasUrls():
            urls = mime_data.urls()
            for url in urls:
                if url.isLocalFile():
                    file_path = url.toLocalFile()
                    if file_path.lower().endswith(('.png', '.jpg', '.bmp', '.gif')):
                        self.insert_image(file_path)

    def print_dialog(self):
        printer = QPrinter()
        dialog = QPrintDialog(printer, self)
        if dialog.exec_() == QPrintDialog.Accepted:
            self.textEdit.print(self.printer)

		
app = QApplication(sys.argv)
myapp = MainScreen()
myapp.show()
sys.exit(app.exec_())
