import socket
import sys
import time
import threading


def server():
    host = socket.gethostname()
    port = 6000
    serveur_socket = socket.socket()
    serveur_socket.bind((host, port))

    serveur_socket.listen(5)
    conn, address = serveur_socket.accept()
    print("Serveur en écoute", str(address))

    data = input(" -> ")
    
    while True:
        data = conn.recv(1024).decode()
        data = data + time.strftime("  reçu à %H:%M:%S")
        print("from Fays: " + str(data))
        if not data:
            break
        data = input(' -> ')
        conn.send(data.encode())
    conn.close()



    










if __name__ == '__main__':
    server()