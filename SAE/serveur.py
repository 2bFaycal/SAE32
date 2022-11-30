import socket
import time
import psutil
import platform


os = platform.system()
ram = psutil.virtual_memory()
cpu = psutil.cpu_percent()
name = socket.gethostname()
ip = socket.gethostbyname(name)


host = socket.gethostname()
port = 6000

serveur_socket = socket.socket()
serveur_socket.bind((host, port))
serveur_socket.listen(5)

print("Serveur en écoute")
conn, address = serveur_socket.accept()
print("Serveur connecté à ", str(address))

msg = ""

while msg != 'bye':

    msg = conn.recv(1024).decode()
    message = msg + time.strftime("  reçu à %H:%M:%S")
    print('from Client: ' + message)

    if msg == 'cpu':
        reply = str(cpu)
        conn.send(str(cpu).encode())
        print("CPU envoyé" + time.strftime("  à %H:%M:%S"))


    elif msg == 'ram':
        reply = str(ram)
        conn.send(str(ram).encode())
        print("RAM envoyé" + time.strftime("  à %H:%M:%S"))
        

    elif msg == 'os':
        reply = str(os)
        conn.send(str(os).encode())
        print("OS envoyé" + time.strftime("  à %H:%M:%S"))


    elif msg == 'name':
        reply = str(name)
        conn.send(str(name).encode())
        print("Name envoyé" + time.strftime("  à %H:%M:%S"))

    
    elif msg == 'ip':
        reply = str(ip)
        conn.send(str(ip).encode())
        print("IP envoyé" + time.strftime("  à %H:%M:%S"))


    else:
        reply = input(" -> ")        
        conn.send(reply.encode())

        msg = conn.recv(1024).decode()
        message = msg + time.strftime("  reçu à %H:%M:%S")        
        print("from Client: " + message)

conn.close()



