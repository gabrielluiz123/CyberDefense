import sys
from SQL import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap


class Sql(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnChoiceSQL.clicked.connect(self.choicesql)
        self.btnSQLVoltar.clicked.connect(self.voltar)

    def choicesql(self):
        pass

    def voltar(self):
        pass


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    sql = Sql()
    sql.show()
    qt.exec()