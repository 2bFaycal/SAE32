import sys
import socket
import time


host = socket.gethostname()
port = 6000

client_socket = socket.socket()
client_socket.connect((host, port))
print("Client connecté au serveur")

data = ""
while data != 'bye':
    message = input(" -> ")
    client_socket.send(message.encode())
    print("message envoyé" + time.strftime("  à %H:%M:%S"))

    data = client_socket.recv(1024).decode()
    dtime = data + time.strftime("  reçu à %H:%M:%S")
    print('from Serv: ' + dtime)


client_socket.close()
print ("Client déconnecté")


