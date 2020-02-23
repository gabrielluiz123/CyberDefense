import sys
from Pass import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap


class Pass(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)


if __name__ == '__PassFile.py__':
    def ex():
        la = QApplication(sys.argv)
        pass1 = Pass()
        pass1.show()
        la.exec()
