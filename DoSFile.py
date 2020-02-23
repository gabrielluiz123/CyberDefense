import sys
from DoS import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap


class DoS(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnDoSChoice.clicked.connect(self.choicedos)
        self.btnDoSVoltar.clicked.connect(self.voltar)

    def choicedos(self):
        pass

    def voltar(self):
        pass


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    dos = DoS()
    dos.show()
    qt.exec()