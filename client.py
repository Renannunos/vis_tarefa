import socket
import time
from datetime import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.1.10"
port = 8000
s.connect((host, port))

def ts(str, r):
    s.send(r.encode())
    data = ''
    data = s.recv(1024).decode()
    print (data)


def tarefa():
    while True:
        r = input('Nome - Tarefa: ')
        if r.lower() == "fim":
            print("Voce saiu do sistema")
            return
        else:
            a = r.split("- ")
            hora = datetime.now()
            c =  hora.strftime('%d/%m/%Y %H:%M')
            b = "Nome: " + a[0] + "\nTarefa: " + a[1] + "\nInício: " + c + "\n\n"
            ts(s,b)


tarefa()
s.close()




