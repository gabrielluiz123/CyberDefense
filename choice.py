import sys
from Pass import *
from SQL import *
from DoS import *
from main import *
import socket
import threading
from datetime import datetime
from PyQt5.QtWidgets import QMainWindow, QApplication


class Choice(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnChoice.clicked.connect(self.choicedef)
        self.btnClose.clicked.connect(self.sair)

    def choicedef(self):
        if int(self.inputChoice.text()) == 1:
            dosChoice.show()
            choice.close()
        elif int(self.inputChoice.text()) == 2:
            passChoice.show()
            choice.close()
        elif int(self.inputChoice.text()) == 3:
            sqlChoice.show()
            choice.close()

    def sair(self):
        choice.close()


class ChoicePass(QMainWindow, Ui_Pass_Window):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnVoltarPass.clicked.connect(self.voltar)
        self.btnChoicePass.clicked.connect(self.escolhapass)
        self.passBork = None
        self.conn = None
        self.data = None
        self.aa = None

        self.dateNow = datetime.now()
        self.dateNow = self.dateNow.strftime('%Y-%m-%d_%H-%M-%S')

    def voltar(self):
        choice.show()
        passChoice.close()

    def escolhapass(self):
        if int(self.inputPass.text()) == 1:
            self.l_defesa_pass.setText(f'A defesa escolhida foi {self.l_pass1.text()}')
            self.passBork = server()
            if self.passBork == '1':
                file = open(f'Password_{self.l_pass1.text()}_{self.dateNow}.txt', 'w+')
                file.write('Defesa contra quebra de senhas funcionou e senha foi protegida contra ataque!\n')
            else:
                file = open(f'Password_{self.l_pass1.text()}__{self.dateNow}.txt', 'w+')
                file.write('Senha foi quebrada!\n')
                file.write(f'{self.passBork}\n')
        elif int(self.inputPass.text()) == 2:
            self.l_defesa_pass.setText(f'A defesa escolhida foi {self.l_pass2.text()}')
            self.passBork = server()
            if self.passBork == '1':
                file = open(f'Password_{self.l_pass1.text()}_{self.dateNow}.txt', 'w+')
                file.write('Defesa contra quebra de senhas funcionou e senha foi protegida contra ataque!\n')
            else:
                file = open(f'Password_{self.l_pass1.text()}__{self.dateNow}.txt', 'w+')
                file.write('Senha foi quebrada!\n')
                file.write(f'{self.passBork}\n')


class ChoiceDos(QMainWindow, Ui_Dos_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pinga = None
        super().setupUi(self)
        self.btnDoSVoltar.clicked.connect(self.voltar)
        self.btnDoSChoice.clicked.connect(self.escolhados)
        self.host = 'curso-gabriel-teste.com.br'
        self.dateNow = datetime.now()
        self.dateNow = self.dateNow.strftime('%Y-%m-%d_%H-%M-%S')

    def voltar(self):
        choice.show()
        dosChoice.close()

    def escolhados(self):
        if int(self.inputDoS.text()) == 1:
            self.l_defesa_dos.setText(f'A defesa escolhida foi {self.l_dos1.text()}')
            self.pinga = self.ping()

            if not self.pinga:
                file = open(f'DoS_{self.l_dos1.text()}__{self.dateNow}.txt', 'w+')
                file.write('Defesa contra DDoS foi quabrada!\n')
            else:
                file = open(f'DoS_{self.l_dos1.text()}__{self.dateNow}.txt', 'w+')
                file.write('Defesa contra DDoS foi feita com sucesso!\n')
                file.write(f'{self.pinga}')
        elif int(self.inputDoS.text()) == 2:
            self.l_defesa_dos.setText(f'A defesa escolhida foi {self.l_dos2.text()}')
            self.pinga = self.ping()

            if self.pinga:
                file = open(f'DoS_{self.l_dos2.text()}__{self.dateNow}.txt', 'w+')
                file.write('Defesa contra DDoS feita com sucesso!\n')
            else:
                file = open(f'DoS_{self.l_dos2.text()}__{self.dateNow}.txt', 'w+')
                file.write('Defesa contra DDoS foi quebrada!\n')

    def ping(self):
        import os, platform

        if platform.system().lower() == "windows":
            ping_str = "-n 1"
        else:
            ping_str = "-c 1"

        resposta = os.system("ping " + ping_str + " " + self.host)
        cmd = "ping -n 1 " + self.host
        r = "".join(os.popen(cmd).readlines())
        r = r.encode('ascii', 'ignore').decode('ascii')
        ping_split = r.split("\n")
        if resposta == 0:
            return f'{ping_split[4]} \n{ping_split[5]} {ping_split[6].strip()} \n Latências após ataque: {ping_split[8]}'
        else:
            return False


class ChoiceSql(QMainWindow, Ui_Sql_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnSQLVoltar.clicked.connect(self.voltar)
        self.btnChoiceSQL.clicked.connect(self.escolhasql)

    def voltar(self):
        choice.show()
        sqlChoice.close()

    def escolhasql(self):
        if int(self.inputSQL.text()) == 1:
            self.l_defesa_sql.setText(f'A defesa escolhida foi {self.l_sql1.text()}')
        elif int(self.inputSQL.text()) == 2:
            self.l_defesa_sql.setText(f'A defesa escolhida foi {self.l_sql2.text()}')


def server(messagem):
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind(('127.0.0.1', 8000))
    serv.listen(5)
    while True:
        conn, addr = serv.accept()
        from_client = ''
        while True:
            data = conn.recv(4096)
            if not data: break
            from_client += data.decode()
            print(from_client)
        conn.close()
        return from_client


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    choice = Choice()
    passChoice = ChoicePass()
    sqlChoice = ChoiceSql()
    dosChoice = ChoiceDos()
    choice.show()
    qt.exec()
