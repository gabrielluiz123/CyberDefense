# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pass.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Pass_Window(object):
    def setupUi(self, Pass_Window):
        Pass_Window.setObjectName("Pass_Window")
        Pass_Window.resize(492, 302)
        self.centralwidget = QtWidgets.QWidget(Pass_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 30, 271, 16))
        self.label.setObjectName("label")
        self.l_pass1 = QtWidgets.QLabel(self.centralwidget)
        self.l_pass1.setGeometry(QtCore.QRect(60, 80, 81, 16))
        self.l_pass1.setObjectName("l_pass1")
        self.l_pass2 = QtWidgets.QLabel(self.centralwidget)
        self.l_pass2.setGeometry(QtCore.QRect(60, 110, 81, 16))
        self.l_pass2.setObjectName("l_pass2")
        self.inputPass = QtWidgets.QLineEdit(self.centralwidget)
        self.inputPass.setGeometry(QtCore.QRect(40, 190, 113, 20))
        self.inputPass.setObjectName("inputPass")
        self.btnChoicePass = QtWidgets.QPushButton(self.centralwidget)
        self.btnChoicePass.setGeometry(QtCore.QRect(160, 190, 75, 23))
        self.btnChoicePass.setObjectName("btnChoicePass")
        self.btnVoltarPass = QtWidgets.QPushButton(self.centralwidget)
        self.btnVoltarPass.setGeometry(QtCore.QRect(250, 190, 75, 23))
        self.btnVoltarPass.setObjectName("btnVoltarPass")
        self.l_defesa_pass = QtWidgets.QLabel(self.centralwidget)
        self.l_defesa_pass.setGeometry(QtCore.QRect(140, 260, 251, 16))
        self.l_defesa_pass.setText("")
        self.l_defesa_pass.setObjectName("l_defesa_pass")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 110, 47, 13))
        self.label_3.setObjectName("label_3")
        Pass_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Pass_Window)
        QtCore.QMetaObject.connectSlotsByName(Pass_Window)

    def retranslateUi(self, Pass_Window):
        _translate = QtCore.QCoreApplication.translate
        Pass_Window.setWindowTitle(_translate("Pass_Window", "MainWindow"))
        self.label.setText(_translate("Pass_Window", "Escolha o software de defesa contra Password cracking"))
        self.l_pass1.setText(_translate("Pass_Window", "password 1"))
        self.l_pass2.setText(_translate("Pass_Window", "password 2"))
        self.btnChoicePass.setText(_translate("Pass_Window", "Escolher"))
        self.btnVoltarPass.setText(_translate("Pass_Window", "Voltar"))
        self.label_2.setText(_translate("Pass_Window", "1 - "))
        self.label_3.setText(_translate("Pass_Window", "2 -"))
