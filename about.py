# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
# import res_rc
import res 


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/res/icons/text-editor.png"))
        Dialog.setWindowIcon(icon)
        
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 12, 381, 271))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "About"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><img src=\":/res/icons/text-editor.png\"/></p><p align=\"center\">Awasome Notepad</p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Author : Tanzim Rizwan</span></p><p align=\"center\"><span style=\" font-size:12pt;\">Build Date : 12-10-17</span></p><p align=\"center\"><span style=\" font-size:12pt;\">Copyright (C) 2017</span></p><p align=\"center\"><span style=\" font-size:12pt;\">Version : 1.0</span></p></body></html>"))


