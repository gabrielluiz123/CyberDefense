import socket
import os
from multiprocessing import Pool
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))
astr = "I am CLIENT<br>".encode()
client.send(astr)
#from_server = client.recv(4096)
client.close()