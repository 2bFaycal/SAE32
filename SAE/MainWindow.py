from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import socket
import time
import psutil
import platform
import os


os = platform.system()
ram = psutil.virtual_memory()
cpu = psutil.cpu_percent()
name = socket.gethostname()
ip = socket.gethostbyname(name)

class client(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("SAE32")

        widget = QWidget()
        self.setCentralWidget(widget)

        grid = QGridLayout()
        widget.setLayout(grid)

        os = QPushButton("OS")
        ram = QPushButton("RAM")
        cpu = QPushButton("CPU")
        ip = QPushButton("IP")
        name = QPushButton("NAME")
        disconnect = QPushButton("DISCONNECT")
        disconnect.clicked.connect(self.close)
        arret = QPushButton("ARRET")
        arret.clicked.connect(self.close)
        self.__ping = QLineEdit("")
        ping1 = QPushButton("PING")
        clear = QPushButton("CLEAR")
 
        self.lab1 = QLabel("")
        self.lab2 = QLabel("")
        self.lab3 = QLabel("")
        self.lab4 = QLabel("")
        self.lab5 = QLabel("")
        self.lab6 = QLabel("")

        grid.addWidget(os, 0, 1, 1, 2)
        grid.addWidget(ram, 2, 1, 1, 2)
        grid.addWidget(cpu, 4, 1, 1, 2)
        grid.addWidget(ip, 6, 1, 1, 2)
        grid.addWidget(name, 8, 1, 1, 2)
        grid.addWidget(disconnect, 10, 1, 1, 2)
        grid.addWidget(arret, 11, 1, 1, 2)
        grid.addWidget(self.__ping, 12, 1, 1, 2)
        grid.addWidget(ping1, 13, 1, 1, 2)
        grid.addWidget(clear, 15, 1, 1, 2)

        grid.addWidget(self.lab1, 1, 2)
        grid.addWidget(self.lab2, 3, 2)
        grid.addWidget(self.lab3, 5, 2)
        grid.addWidget(self.lab4, 7, 2)
        grid.addWidget(self.lab5, 9, 2)
        grid.addWidget(self.lab6, 14, 1, 1, 2)

        os.clicked.connect(self.__actionOS)
        ram.clicked.connect(self.__actionRAM)
        cpu.clicked.connect(self.__actionCPU)
        ip.clicked.connect(self.__actionIP)
        name.clicked.connect(self.__actionNAME)
        arret.clicked.connect(self.__actionARRET)
        ping1.clicked.connect(self.__actionPING)
        clear.clicked.connect(self.__actionCLEAR)


    def __actionOS(self):
        message = "os"
        client_socket.send(message.encode())       
        print("requête os envoyée")
        data = client_socket.recv(1024).decode()
        dtime = data + time.strftime(" reçu à %H:%M", time.localtime())
        self.lab1.setText(dtime)


    def __actionRAM(self):
        message = "ram"
        client_socket.send(message.encode())    
        print ('requête ram envoyée')
        data = client_socket.recv(1024).decode()
        dtime = data + time.strftime("  reçu à %H:%M")
        self.lab2.setText(dtime)


    def __actionCPU(self):
        message = "cpu"
        client_socket.send(message.encode())
        print ('requête cpu envoyée')
        data = client_socket.recv(1024).decode()
        dtime = data + time.strftime("  reçu à %H:%M")
        self.lab3.setText(dtime)


    def __actionIP(self):
        message = "ip"
        client_socket.send(message.encode())
        print ('requête ip envoyé')
        data = client_socket.recv(1024).decode()
        dtime = data + time.strftime("  reçu à %H:%M")
        self.lab4.setText(dtime)


    def __actionNAME(self):
        message = "name"
        client_socket.send(message.encode())
        print ('requête name envoyé')
        data = client_socket.recv(1024).decode()
        dtime = data + time.strftime("  reçu à %H:%M")
        self.lab5.setText(dtime)


    def __actionARRET(self):
        message = "arret"
        client_socket.send(message.encode())
        print ('requête arret envoyé')
        data = client_socket.recv(1024).decode()
        dtime = data + time.strftime("  reçu à %H:%M")


    def __actionPING(self):
        message = "ping " + self.__ping.text()
        print (message)
        client_socket.send(message.encode())
        print ('ping envoyé')
        data = client_socket.recv(1024).decode()
        dtime = data + time.strftime("  reçu à %H:%M")
        self.lab6.setText(dtime)


    def __actionCLEAR(self):
        self.lab1.setText("")
        self.lab2.setText("")
        self.lab3.setText("")
        self.lab4.setText("")
        self.lab5.setText("")
        self.lab6.setText("")

        
if __name__ == "__main__":

    host = socket.gethostname()
    port = 6000

    print("client se connecte au serveur")
    client_socket = socket.socket()

    client_socket.connect((host, port))
    print("Client connecté au serveur")

    app = QApplication(sys.argv)

    window = client()
    window.show()
    app.exec()

    