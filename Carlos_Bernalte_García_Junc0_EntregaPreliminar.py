from socket import *
import sys
import traceback


reto0=("node1",2000)
reto1=("node1",3000)
reto2=("node1",4000)
reto3=("node1",5001)

lista_sockets=[]

def comprobar_respuesta(sock):
    resp=sock.recv(2048).decode()
    if resp[0]== "c":
        return resp
    else:
        return comprobar_respuesta(sock)

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

    sock_reto2.send((str(identificador2)+" "+str(numero_de_espacios)).encode())
    resp_reto2=comprobar_respuesta(sock_reto2)
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

def main():
    Reto_3(Reto_2(Reto_1(Reto_0())))
 

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
        

