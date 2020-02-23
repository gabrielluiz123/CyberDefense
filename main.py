# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(486, 359)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LableTitle = QtWidgets.QLabel(self.centralwidget)
        self.LableTitle.setGeometry(QtCore.QRect(140, 40, 181, 16))
        self.LableTitle.setObjectName("LableTitle")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 110, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 150, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 200, 91, 16))
        self.label_3.setObjectName("label_3")
        self.inputChoice = QtWidgets.QLineEdit(self.centralwidget)
        self.inputChoice.setGeometry(QtCore.QRect(40, 260, 171, 20))
        self.inputChoice.setObjectName("inputChoice")
        self.btnChoice = QtWidgets.QPushButton(self.centralwidget)
        self.btnChoice.setGeometry(QtCore.QRect(230, 260, 75, 23))
        self.btnChoice.setObjectName("btnChoice")
        self.btnClose = QtWidgets.QPushButton(self.centralwidget)
        self.btnClose.setGeometry(QtCore.QRect(310, 260, 75, 23))
        self.btnClose.setObjectName("btnClose")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simulador de Defesa Cibernética"))
        self.LableTitle.setText(_translate("MainWindow", "Escolha o Tipo de defesa para testar"))
        self.label.setText(_translate("MainWindow", "1 - DoS"))
        self.label_2.setText(_translate("MainWindow", "2 - Password Cracking"))
        self.label_3.setText(_translate("MainWindow", "3 - SQL Injection"))
        self.btnChoice.setText(_translate("MainWindow", "Escolher"))
        self.btnClose.setText(_translate("MainWindow", "Sair"))
