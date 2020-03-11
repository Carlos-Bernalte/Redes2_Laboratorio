import socket

def main():
        servidor=("node1",2000)
        minombre="carlos.bernalte"
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(servidor)
        print(sock.recv(1024).decode()) #Recibir instrucciones
        sock.send(minombre.encode())    #Enviar informacion
        print(sock.recv(1024).decode()) #Recibir respuesta  del servidor final
        sock.close()

try:
    main()
except KeyboardInterrupt:
    pass
