import sys
import os
from Pass import *
from SQL import *
from DoS import *
from main import *
import threading
import time
import concurrent.futures
import socket
from datetime import datetime
from PyQt5.QtWidgets import QMainWindow, QApplication
import pymysql.cursors

conexao = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='',
    db='sitedjango',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = conexao.cursor()


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

        self.dateNow = datetime.now()
        self.dateNow = self.dateNow.strftime('%Y-%m-%d_%H-%M-%S')

    def voltar(self):
        choice.show()
        passChoice.close()

    def escolhapass(self):
        if int(self.inputPass.text()) == 1:
            self.l_defesa_pass.setText(f'A defesa escolhida foi {self.l_pass1.text()}')
            cursor.execute('UPDATE auth_user set password = "pbkdf2_sha256$150000$vzUeGZiV8aS2$GqmNqQZpc6Qt3TpidP3VFjGz/hZAuxtqOFeHhPHFYD4=" where id = "1"')
        elif int(self.inputPass.text()) == 2:
            self.l_defesa_pass.setText(f'A defesa escolhida foi {self.l_pass2.text()}')
            os.rename('C:/Agenda/agenda/settings.py', 'C:/Agenda/contatos/settingsOriginal.py')
            os.rename('C:/Agenda/agenda/settingsAxes.py', 'C:/Agenda/contatos/settings.py')
        else:

            self.l_defesa_pass.setText(f'Não foi selecionada nenhuma defesa')
        threading.Thread(target=self.download).start()

    def download(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(self.server, 'world!')
            return_value = future.result()
            return_value = return_value.split('|')
            if int(self.inputPass.text()) == 1:
                self.l_defesa_pass.setText(f'A defesa escolhida foi {self.l_pass1.text()}')
                if return_value[0] == '1':
                    file = open(f'Password_{self.l_pass1.text()}_{self.dateNow}.txt', 'w+')
                    file.write('Defesa contra quebra de senhas funcionou e senha foi protegida contra ataque!\n')
                    file.write(f'Tempo de tentativa: {return_value[1]}\n')
                    file.write(f'Ataque utilizado: {return_value[2]}\n')
                else:
                    file = open(f'Password_{self.l_pass1.text()}__{self.dateNow}.txt', 'w+')
                    file.write('Senha foi quebrada!\n')
                    file.write(f'Senha quebrada em: {return_value[1]}\n')
                    file.write(f'Ataque utilizado: {return_value[2]}\n')
                cursor.execute('UPDATE auth_user set password = "pbkdf2_sha256$150000$x4Rd6FH9Y4ce$7fW82ri3M/RYwHJGRgIrqYsa0fH5PvOzKrD4YmhPzjM=" where id = "1"')
            elif int(self.inputPass.text()) == 2:
                self.l_defesa_pass.setText(f'A defesa escolhida foi {self.l_pass2.text()}')
                if return_value[0] == '1':
                    file = open(f'Password_{self.l_pass2.text()}_{self.dateNow}.txt', 'w+')
                    file.write('Defesa contra quebra de senhas funcionou e senha foi protegida contra ataque!\n')
                    file.write(f'Tempo de tentativa: {return_value[1]}\n')
                    file.write(f'Ataque utilizado: {return_value[2]}\n')
                else:
                    file = open(f'Password_{self.l_pass2.text()}__{self.dateNow}.txt', 'w+')
                    file.write('Senha foi quebrada!\n')
                    file.write(f'Senha quebrada em: {return_value[1]}\n')
                    file.write(f'Ataque utilizado: {return_value[2]}\n')
                os.rename('C:/Agenda/agenda/settings.py', 'C:/Agenda/contatos/settingsAxes.py')
                os.rename('C:/Agenda/agenda/settingsOriginal.py', 'C:/Agenda/contatos/settings.py')
            else:
                if return_value[0] == '1':
                    file = open(f'Password_{self.l_pass2.text()}_{self.dateNow}.txt', 'w+')
                    file.write('Defesa contra quebra de senhas funcionou e senha foi protegida contra ataque!\n')
                    file.write(f'Tempo de tentativa: {return_value[1]}\n')
                    file.write(f'Ataque utilizado: {return_value[2]}\n')
                else:
                    file = open(f'Password_{self.l_pass2.text()}__{self.dateNow}.txt', 'w+')
                    file.write('Senha foi quebrada!\n')
                    file.write(f'Senha quebrada em: {return_value[1]}\n')
                    file.write(f'Ataque utilizado: {return_value[2]}\n')
            return return_value

    def server(messagem, *args):
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

            conn.close()
            return from_client


class ChoiceDos(QMainWindow, Ui_Dos_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pinga = None
        super().setupUi(self)
        self.btnDoSVoltar.clicked.connect(self.voltar)
        self.btnDoSChoice.clicked.connect(self.escolhados)
        self.host = '127.0.0.1'
        self.dateNow = datetime.now()
        self.dateNow = self.dateNow.strftime('%Y-%m-%d_%H-%M-%S')
        self.conn = None
        self.file = None

    def voltar(self):
        choice.show()
        self.conn.close()
        dosChoice.close()

    def escolhados(self):

        if int(self.inputDoS.text()) == 1:
            self.pinga = self.ping()
            name = f'DoS_{self.l_dos1.text()}__{self.dateNow}.txt'
            self.l_defesa_dos.setText(f'A defesa escolhida foi {self.l_dos1.text()}')
            file = open(name, 'w+')

        elif int(self.inputDoS.text()) == 2:
            self.pinga = self.ping()
            name = f'DoS_{self.l_dos2.text()}__{self.dateNow}.txt'
            self.l_defesa_dos.setText(f'A defesa escolhida foi {self.l_dos2.text()}')
            file = open(name, 'w+')
        else:
            self.pinga = self.ping()
            self.l_defesa_dos.setText(f'Sem defesa escolhida')
            name = f'DoS_Original__{self.dateNow}.txt'
            file = open(name, 'w+')
        file.write('Ping antes do ataque:!\n')
        file.write(f'{self.pinga}')
        threading.Thread(target=self.download, args=(name,)).start()


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
            return f'{ping_split[4]} \n{ping_split[5]} {ping_split[6].strip()} \n Latências: {ping_split[8]}\n'
        else:
            return False

    def download(self, name):
        file = open(name, 'r')
        conteudo = file.readlines()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(self.server, 'world!')
            return_value = future.result()
            if not self.pinga:
                conteudo.append('Defesa contra DDoS foi quabrada e o servidor caiu!\n')
                conteudo.append(f'Ataque utilizado:{return_value}!\n')
            else:
                conteudo.append('Defesa contra DDoS foi feita com sucesso!\n')
                conteudo.append('Ping depois do ataque!\n')
                conteudo.append(f'{self.pinga}')
                conteudo.append(f'\nAtaque utilizado:{return_value}!\n')
                arquivo = open(name, 'w')
                arquivo.writelines(conteudo)
            return return_value

    def server(messagem, *args):
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

            conn.close()
            return from_client


class ChoiceSql(QMainWindow, Ui_Sql_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnSQLVoltar.clicked.connect(self.voltar)
        self.btnChoiceSQL.clicked.connect(self.escolhasql)

        self.dateNow = datetime.now()
        self.dateNow = self.dateNow.strftime('%Y-%m-%d_%H-%M-%S')
        self.sqlBork = None
        self.resultado1 = None
        self.resultado2 = None

    def voltar(self):
        choice.show()
        sqlChoice.close()

    def escolhasql(self):
        cursor.execute('SELECT * FROM contatos_categoria')
        self.resultado1 = cursor.fetchall()
        self.resultado1 = len(self.resultado1)

        if int(self.inputSQL.text()) == 1:
            os.rename('C:/Agenda/contatos/views.py', 'C:/Agenda/contatos/viewsOriginal.py')
            os.rename('C:/Agenda/contatos/viewsORM.py', 'C:/Agenda/contatos/views.py')
            self.l_defesa_sql.setText(f'A defesa escolhida foi {self.l_sql1.text()}')
            threading.Thread(target=self.download).start()
        elif int(self.inputSQL.text()) == 2:
            os.rename('C:/Agenda/contatos/views.py', 'C:/Agenda/contatos/viewsOriginal.py')
            os.rename('C:/Agenda/contatos/viewsORM.py', 'C:/Agenda/contatos/views.py')
            self.l_defesa_sql.setText(f'A defesa escolhida foi {self.l_sql2.text()}')
            threading.Thread(target=self.download).start()
        else:
            self.l_defesa_sql.setText(f'Não foi escolhida nenhuma defesa')
            threading.Thread(target=self.download).start()

    def download(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(self.server, 'world!')
            return_value = future.result()
            cursor.execute('SELECT * FROM contatos_categoria')
            self.resultado2 = cursor.fetchall()
            self.resultado2 = len(self.resultado2)
            result = self.resultado2 - self.resultado1
            if self.resultado1 == self.resultado2:
                if int(self.inputSQL.text()) == 1:
                    file = open(f'SQL_{self.l_sql1.text()}_{self.dateNow}.txt', 'w+')
                file.write('Defesa contra SQL Injection funcionou e o banco foi protegido contra ataque!\n')
                os.rename('C:/Agenda/contatos/views.py', 'C:/Agenda/contatos/viewsORM.py')
                os.rename('C:/Agenda/contatos/viewsOriginal.py', 'C:/Agenda/contatos/views.py')
            else:
                if int(self.inputSQL.text()) == 1:
                    file = open(f'SQL_{self.l_sql1.text()}__{self.dateNow}.txt', 'w+')
                elif int(self.inputSQL.text()) == 2:
                    file = open(f'SQL_{self.l_sql2.text()}__{self.dateNow}.txt', 'w+')
                else:
                    file = open(f'SQL_Original__{self.dateNow}.txt', 'w+')
                file.write('SQL Injection aplicado!\n')
                file.write(f'foram inseridos {result} registros no banco\n')
                file.write(f'{self.return_value}\n')
                os.rename('C:/Agenda/contatos/views.py', 'C:/Agenda/contatos/viewsORM.py')
                os.rename('C:/Agenda/contatos/viewsOriginal.py', 'C:/Agenda/contatos/views.py')
            return return_value
    def server(messagem, *args):
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

            return from_client


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    choice = Choice()
    passChoice = ChoicePass()
    sqlChoice = ChoiceSql()
    dosChoice = ChoiceDos()
    choice.show()
    qt.exec()
