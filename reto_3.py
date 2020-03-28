from socket import *
import time

reto0=("node1",2000)
reto1=("node1",3000)
reto2=("node1",4000)
reto3=("node1",5001)
minombre="carlos.bernalte" #Del reto 0
mi_puerto=8989 #Del reto 1

#______________________________________RETO 0__________________________________#
sock_reto0= socket(AF_INET, SOCK_STREAM)
sock_reto0.connect(reto0)

print(sock_reto0.recv(1024).decode())        #Recibir instrucciones
sock_reto0.send(minombre.encode())           #Enviar informacion
resp_reto0=sock_reto0.recv(1024).decode()      #Recibir respuesta con identificador del servidor final
print(resp_reto0)  
indentificador1=resp_reto0[0:36]
sock_reto0.close()

#______________________________________RETO 1__________________________________#
sock_reto1= socket(AF_INET, SOCK_DGRAM)
sock_reto1.bind(('', mi_puerto))

sock_reto1.sendto((str(mi_puerto)+" "+str(indentificador1)).encode(),reto1)#Enviar identificador con puerto
resp_reto1=sock_reto1.recvfrom(1024)[0].decode()
print(resp_reto1)
indentificador2=resp_reto1[5:41]
sock_reto1.close()

#______________________________________RETO 2__________________________________#

sock_reto2= socket(AF_INET, SOCK_STREAM)
sock_reto2.connect(reto2)
finded=1
numero_de_espacios=0
while 1:
    msg=sock_reto2.recv(1024).decode()
    
    if msg.find("that's all")==-1:
        numero_de_espacios=numero_de_espacios+msg.count(" ")+msg.count("\n")+msg.count("\t")
    else:
        position=msg.find("that's all")
        numero_de_espacios=numero_de_espacios+msg[0:position].count(" ")+msg[0:position].count("\n")+msg[0:position].count("\t")
        break

sock_reto2.send((str(indentificador2)+" "+str(numero_de_espacios)).encode())
sock_reto2.recv(2048)
resp_reto2=sock_reto2.recv(2048).decode()
indentificador3=resp_reto2[5:41]
print(resp_reto2)
sock_reto2.close()

#______________________________________RETO 3__________________________________#

sock_reto3= socket(AF_INET, SOCK_STREAM)
sock_reto3.connect(reto3)
suma_total=0
while 1:
    msg=sock_reto3.recv(1024).decode()
    respuesta_en_vector=msg.split()
    for X in respuesta_en_vector:
        if(X.isdigit()):
            suma_total=suma_total+int(X)
            if(suma_total>1300): break
        else:
            palabra=X
    if(suma_total>1300): break

sock_reto3.send((str(palabra)+" "+str(indentificador3)).encode())
resp_reto3=sock_reto3.recv(2048).decode()

print(sock_reto3.recv(2048).decode())
sock_reto3.close()
