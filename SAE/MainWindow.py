from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import socket
import time
import psutil
import platform

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
        quit = QPushButton("QUIT")
        quit.clicked.connect(self.close)
 
        self.lab1 = QLabel()
        self.lab2 = QLabel()
        self.lab3 = QLabel()
        self.lab4 = QLabel()
        self.lab5 = QLabel()


        grid.addWidget(os, 0, 1, 1, 2)
        grid.addWidget(ram, 2, 1, 1, 2)
        grid.addWidget(cpu, 4, 1, 1, 2)
        grid.addWidget(ip, 6, 1, 1, 2)
        grid.addWidget(name, 8, 1, 1, 2)
        grid.addWidget(disconnect, 10, 1, 1, 2)
        grid.addWidget(quit, 12, 1, 1, 2)

        grid.addWidget(self.lab1, 1, 2)
        grid.addWidget(self.lab2, 3, 2)
        grid.addWidget(self.lab3, 5, 2)
        grid.addWidget(self.lab4, 7, 2)
        grid.addWidget(self.lab5, 9, 2)



        def __actionOS():
            message = "os"
            client_socket.send(message.encode())

            print ('os envoyé')
            data = client_socket.recv(1024).decode()
            dtime = data + time.strftime("  reçu à %H:%M:%S")
            self.lab1.setText(dtime)


        def __actionRAM():
            message = "ram"
            client_socket.send(message.encode())

            print ('ram envoyé')
            data = client_socket.recv(1024).decode()
            dtime = data + time.strftime("  reçu à %H:%M:%S")
            self.lab2.setText(dtime)


        def __actionCPU():
            message = "cpu"
            client_socket.send(message.encode())

            print ('cpu envoyé')
            data = client_socket.recv(1024).decode()
            dtime = data + time.strftime("  reçu à %H:%M:%S")
            self.lab3.setText(dtime)


        def __actionIP():
            message = "ip"
            client_socket.send(message.encode())

            print ('ip envoyé')
            data = client_socket.recv(1024).decode()
            dtime = data + time.strftime("  reçu à %H:%M:%S")
            self.lab4.setText(dtime)


        def __actionNAME():
            message = "name"
            client_socket.send(message.encode())

            print ('name envoyé')
            data = client_socket.recv(1024).decode()
            dtime = data + time.strftime("  reçu à %H:%M:%S")
            self.lab5.setText(dtime)


        def __actionDISCONNECT():
            message = "bye"
            client_socket.send(message.encode())

            print ('bye envoyé')
            data = client_socket.recv(1024).decode()
            dtime = data + time.strftime("  reçu à %H:%M:%S")
            self.sortie.setText(dtime)
            print ("Client déconnecté")
            client_socket.close()
            sys.exit()




        

        

    



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