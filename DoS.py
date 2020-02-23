# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DoS.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dos_MainWindow(object):
    def setupUi(self, Dos_MainWindow):
        Dos_MainWindow.setObjectName("Dos_MainWindow")
        Dos_MainWindow.resize(471, 307)
        self.centralwidget = QtWidgets.QWidget(Dos_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 20, 201, 20))
        self.label.setObjectName("label")
        self.l_dos1 = QtWidgets.QLabel(self.centralwidget)
        self.l_dos1.setGeometry(QtCore.QRect(90, 80, 47, 13))
        self.l_dos1.setObjectName("l_dos1")
        self.l_dos2 = QtWidgets.QLabel(self.centralwidget)
        self.l_dos2.setGeometry(QtCore.QRect(90, 110, 47, 13))
        self.l_dos2.setObjectName("l_dos2")
        self.inputDoS = QtWidgets.QLineEdit(self.centralwidget)
        self.inputDoS.setGeometry(QtCore.QRect(70, 180, 113, 20))
        self.inputDoS.setObjectName("inputDoS")
        self.btnDoSChoice = QtWidgets.QPushButton(self.centralwidget)
        self.btnDoSChoice.setGeometry(QtCore.QRect(190, 180, 75, 23))
        self.btnDoSChoice.setObjectName("btnDoSChoice")
        self.btnDoSVoltar = QtWidgets.QPushButton(self.centralwidget)
        self.btnDoSVoltar.setGeometry(QtCore.QRect(290, 180, 75, 23))
        self.btnDoSVoltar.setObjectName("btnDoSVoltar")
        self.l_defesa_dos = QtWidgets.QLabel(self.centralwidget)
        self.l_defesa_dos.setGeometry(QtCore.QRect(120, 230, 291, 20))
        self.l_defesa_dos.setText("")
        self.l_defesa_dos.setObjectName("l_defesa_dos")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 80, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 110, 47, 13))
        self.label_3.setObjectName("label_3")
        Dos_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Dos_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 471, 21))
        self.menubar.setObjectName("menubar")
        Dos_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Dos_MainWindow)
        self.statusbar.setObjectName("statusbar")
        Dos_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(Dos_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(Dos_MainWindow)

    def retranslateUi(self, Dos_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        Dos_MainWindow.setWindowTitle(_translate("Dos_MainWindow", "DoS"))
        self.label.setText(_translate("Dos_MainWindow", "Escolha o software de defesa contra DoS"))
        self.l_dos1.setText(_translate("Dos_MainWindow", "DoS 1"))
        self.l_dos2.setText(_translate("Dos_MainWindow", "DoS 2"))
        self.btnDoSChoice.setText(_translate("Dos_MainWindow", "Escolher"))
        self.btnDoSVoltar.setText(_translate("Dos_MainWindow", "Voltar"))
        self.label_2.setText(_translate("Dos_MainWindow", "1 -"))
        self.label_3.setText(_translate("Dos_MainWindow", "2 -"))
