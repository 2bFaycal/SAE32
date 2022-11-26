import socket
import sys
import time
import threading


def client():
    host = socket.gethostname()
    port = 6000
    client_socket = socket.socket()
    client_socket.connect((host, port))
    print("Client connecté au serveur")





    message = input(" -> ")

    while message.lower().strip() != 'stop':
        client_socket.send(message.encode())
        client_socket.send(time.strftime("  envoyé à %H:%M:%S").encode())
        data = client_socket.recv(1024).decode()


        print('from Serv: ' + data)
        message = input(" -> ")
    client_socket.close()














if __name__ == '__main__':
    client()





















#python3 C:\Users\fayca\OneDrive\Documents\GitHub\SAE32\SAE\client.py