import socket
from threading import *
import time

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.1.10"
port = 8000
print(host)
print(port)
serversocket.bind((host, port))

class client(Thread):
    def __init__ (self, socket, address):
        Thread.__init__ (self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            arquivo = open('Gerenciador.txt','a')
            arquivo.write(self.sock.recv(1024).decode())
            arquivo.close()
            arquivo = open('Gerenciador.txt','r')
            for linha in arquivo:
                linha = linha.rstrip()
                print (linha)
            arquivo.close()
            print(self.sock.recv(1024).decode())
            self.sock.send(b'RECEBIDO')
           

serversocket.listen(5)
print('Server started and listening')

while 1:
    clientsocket, address = serversocket.accept()
    client(clientsocket, address)
    



  
