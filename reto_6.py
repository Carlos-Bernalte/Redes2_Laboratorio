from socket import *
import sys
import traceback
import struct
import hashlib
import base64
import codecs

#SERVIDORES
reto0=("node1",2000)
reto1=("node1",3000)
reto2=("node1",4000)
reto3=("node1",5001)
reto4=("node1",10001)
reto5=("node1",7001)
reto6=("node1",8002)

lista_sockets=[]

def comprobar_respuesta(sock):
    while 1:
        resp=sock.recv(2048).decode()
        if resp[0:5]== "code:": break
        print("DESCARTED")
    return resp

def enviar_resp(sock, info):
    try:
        sock.send(info)
        return comprobar_respuesta(sock)
    except socket.timeout:
        print("+++++++++++++++++++++++++++++++TIMEOUT+++++++++++++++++++++++++++++++++++++++")
        enviar_resp(sock,info)

def Reto_0():
    sock_reto0= socket(AF_INET, SOCK_STREAM)
    sock_reto0.connect(reto0)
    lista_sockets.append(sock_reto0)

    print(sock_reto0.recv(1024).decode())       
    sock_reto0.send("carlos.bernalte".encode())   
    resp_reto0=sock_reto0.recv(1024).decode()     
    print(resp_reto0)  
    sock_reto0.close()
    return resp_reto0[0:36]


def Reto_1(identificador1):
    sock_reto1= socket(AF_INET, SOCK_DGRAM)
    mi_puerto=8989
    sock_reto1.bind(('', mi_puerto))
    lista_sockets.append(sock_reto1)

    sock_reto1.sendto((str(mi_puerto)+" "+str(identificador1)).encode(),reto1)
    resp_reto1=comprobar_respuesta(sock_reto1)
    print(resp_reto1)
    sock_reto1.close()
    return resp_reto1[5:41]
    

def Reto_2(identificador2):
    sock_reto2= socket(AF_INET, SOCK_STREAM)
    sock_reto2.connect(reto2)
    sock_reto2.settimeout(5)
    lista_sockets.append(sock_reto2)

    numero_de_espacios=0
    while 1:
        msg=sock_reto2.recv(1024).decode()
        
        if msg.find("that's all")==-1:
            numero_de_espacios=numero_de_espacios+msg.count(" ")+msg.count("\n")+msg.count("\t")
        else:
            position=msg.find("that's all")
            numero_de_espacios=numero_de_espacios+msg[0:position].count(" ")+msg[0:position].count("\n")+msg[0:position].count("\t")
            break

    #sock_reto2.send((str(identificador2)+" "+str(numero_de_espacios)).encode())
    resp_reto2=enviar_resp(sock_reto2,(str(identificador2)+" "+str(numero_de_espacios)).encode())
    #resp_reto2=comprobar_respuesta(sock_reto2)
    print(resp_reto2)
    sock_reto2.close()
    return resp_reto2[5:41]


def Reto_3(identificador3):
    sock_reto3= socket(AF_INET, SOCK_STREAM)
    sock_reto3.connect(reto3)
    lista_sockets.append(sock_reto3)

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

    sock_reto3.send((str(palabra)+" "+str(identificador3)).encode())
    resp_reto3=comprobar_respuesta(sock_reto3)
    print(resp_reto3)
    sock_reto3.close()
    return resp_reto3[5:41]

#______________________________________RETO 4__________________________________#
def Reto_4(identificador4):
    sock_reto4= socket(AF_INET, SOCK_STREAM)
    sock_reto4.settimeout(5)
    sock_reto4.connect(reto4)
    lista_sockets.append(sock_reto4)

    sock_reto4.send((identificador4).encode())
    Total_size4=""
    while 1:
        msg4=sock_reto4.recv(1).decode()
        if msg4==":":
            break
        else:
            Total_size4=Total_size4+str(msg4)

    archivo=b''
    while 1:
        archivo_parte=sock_reto4.recv(2048)
        archivo=archivo+archivo_parte
        if len(archivo)==int(Total_size4):
            sha1 = hashlib.sha1(archivo)
            break
    
    #sock_reto4.send(sha1.digest())
    resp_reto4=enviar_resp(sock_reto4, sha1.digest())
    #resp_reto4=comprobar_respuesta(sock_reto4)
    print(resp_reto4)
    sock_reto4.close()
    return resp_reto4[5:41]

def sum16(data):
    if len(data) % 2:
        data = b'\0' + data

    return sum(struct.unpack('!%sH' % (len(data) // 2), data))


def cksum(data):
    sum_as_16b_words  = sum16(data)
    sum_1s_complement = sum16(struct.pack('!L', sum_as_16b_words))
    _1s_complement    = ~sum_1s_complement & 0xffff
    return _1s_complement

#______________________________________RETO 5__________________________________#
def Reto_5(identificador5):
    sock_reto5= socket(AF_INET, SOCK_DGRAM)
    lista_sockets.append(sock_reto5)
    request_=b'WYP\x00\x00\x00\x00\x00'+base64.b64encode(identificador5.encode())
    
    checksum=cksum(request_)

    request=struct.pack("!3sbHH"+str(len(base64.b64encode(identificador5.encode())))+"s",b'WYP',0,0,checksum,base64.b64encode(identificador5.encode()))
    sock_reto5.sendto(request,reto5)
    reply=sock_reto5.recvfrom(5000)[0]

    payload=struct.unpack("!"+str(len(reply[8:]))+"s",reply[8:])
    resp_reto5=base64.b64decode(payload[0]).decode()
    
    print(resp_reto5)
   
    sock_reto5.close()
    return resp_reto5[5:41]

def Reto_6(identificador6):
    port=8134
    sock_reto6_1= socket(AF_INET, SOCK_STREAM)
    lista_sockets.append(sock_reto6_1)
    sock_reto6_1.connect(reto6)
    sock_reto6_1.send((str(identificador6)+" "+str(port)).encode())
    print(sock_reto6_1.recv(4000).decode())
    sock_reto6_1.close()
    """--------------------------------------------------------------------"""
    sock_reto6= socket(AF_INET, SOCK_STREAM)
    sock_reto6.bind(("localhost",port))
    sock_reto6.listen(2)
    print("HOLA QUE TAL?")
    while 1:
        child_sock, client = sock_reto6.accept()
        handle(child_sock, client)
    sock_reto6.close()

def handle(sock, client):
    print('Client connected: {0}'.format(client))
   
    print(sock.recv(1024))
        

    sock.close()
    print('Client disconnected: {0}'.format(client))

def main():
    identificador=Reto_0()
    identificador=Reto_1(identificador)
    identificador=Reto_2(identificador)
    identificador=Reto_3(identificador)
    identificador=Reto_4(identificador)
    identificador=Reto_5(identificador)
    Reto_6(identificador)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        for sock in lista_sockets:
            sock.close()
        print('\nInterrupted (Ctrl + C).')
        exit(0)
    except Exception as ex:
        print("EXCEPTION CATCHED")
        traceback.print_exc()
        
        for sock in lista_sockets:
            sock.close()




"""
def Reto_6(identificador6):
    port=8134
    sock_reto6_1= socket(AF_INET, SOCK_STREAM)
    lista_sockets.append(sock_reto6_1)
    sock_reto6_1.connect(reto6)
    sock_reto6_1.send((str(identificador6)+" "+str(port)).encode())
    print(sock_reto6_1.recv(4000).decode())
    sock_reto6_1.close()
    """--------------------------------------------------------------------"""
    sock_reto6= socket(AF_INET, SOCK_STREAM)
    sock_reto6.bind(("localhost",port))
    sock_reto6.listen(2)
    print("HOLA QUE TAL?")
    while 1:
        child_sock, client = sock_reto6.accept()
        handle(child_sock, client)
    sock_reto6.close()
"""