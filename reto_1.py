from socket import *


reto0=("node1",2000)
reto1=("node1",3000)
minombre="carlos.bernalte"
mi_puerto=8989

sock_TCP= socket(AF_INET, SOCK_STREAM)
sock_TCP.connect(reto0)

sock_UDP= socket(AF_INET, SOCK_DGRAM)
sock_UDP.bind(('', mi_puerto))

#______________________________________RETO 0__________________________________#
print(sock_TCP.recv(1024).decode("utf-8"))        #Recibir instrucciones
sock_TCP.send(minombre.encode("utf-8"))           #Enviar informacion
resp_TCP=sock_TCP.recv(1024).decode("utf-8")      #Recibir respuesta con identificador del servidor final
print("INSTRUCCIONES RETO 1: "+str(resp_TCP))     
indentificador=resp_TCP[0:36]
sock_TCP.close()

#______________________________________RETO 1__________________________________#
reto1=("node1",3000)

sock_UDP.sendto((str(mi_puerto)+" "+str(indentificador)).encode("utf-8"),reto1)#Enviar identificador con puerto
print(str(sock_UDP.recvfrom(1024)[0].decode("utf-8")))
sock_UDP.close()


