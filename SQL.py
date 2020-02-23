# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SQL.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Sql_MainWindow(object):
    def setupUi(self, Sql_MainWindow):
        Sql_MainWindow.setObjectName("Sql_MainWindow")
        Sql_MainWindow.resize(490, 325)
        self.centralwidget = QtWidgets.QWidget(Sql_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 30, 251, 16))
        self.label.setObjectName("label")
        self.l_sql1 = QtWidgets.QLabel(self.centralwidget)
        self.l_sql1.setGeometry(QtCore.QRect(50, 80, 91, 16))
        self.l_sql1.setObjectName("l_sql1")
        self.l_sql2 = QtWidgets.QLabel(self.centralwidget)
        self.l_sql2.setGeometry(QtCore.QRect(50, 110, 91, 16))
        self.l_sql2.setObjectName("l_sql2")
        self.inputSQL = QtWidgets.QLineEdit(self.centralwidget)
        self.inputSQL.setGeometry(QtCore.QRect(40, 200, 113, 20))
        self.inputSQL.setObjectName("inputSQL")
        self.btnChoiceSQL = QtWidgets.QPushButton(self.centralwidget)
        self.btnChoiceSQL.setGeometry(QtCore.QRect(160, 200, 75, 23))
        self.btnChoiceSQL.setObjectName("btnChoiceSQL")
        self.btnSQLVoltar = QtWidgets.QPushButton(self.centralwidget)
        self.btnSQLVoltar.setGeometry(QtCore.QRect(260, 200, 75, 23))
        self.btnSQLVoltar.setObjectName("btnSQLVoltar")
        self.l_defesa_sql = QtWidgets.QLabel(self.centralwidget)
        self.l_defesa_sql.setGeometry(QtCore.QRect(90, 260, 221, 16))
        self.l_defesa_sql.setText("")
        self.l_defesa_sql.setObjectName("l_defesa_sql")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 47, 13))
        self.label_3.setObjectName("label_3")
        Sql_MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(Sql_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(Sql_MainWindow)

    def retranslateUi(self, Sql_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        Sql_MainWindow.setWindowTitle(_translate("Sql_MainWindow", "SQL Injection"))
        self.label.setText(_translate("Sql_MainWindow", "Escolha o software de defesa contra SQL Injection"))
        self.l_sql1.setText(_translate("Sql_MainWindow", "SQL Injection 1"))
        self.l_sql2.setText(_translate("Sql_MainWindow", "SQL Injection 2"))
        self.btnChoiceSQL.setText(_translate("Sql_MainWindow", "Escolher"))
        self.btnSQLVoltar.setText(_translate("Sql_MainWindow", "Voltar"))
        self.label_2.setText(_translate("Sql_MainWindow", "1 -"))
        self.label_3.setText(_translate("Sql_MainWindow", "2 -"))
