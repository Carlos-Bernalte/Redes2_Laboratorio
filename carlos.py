#!/usr/bin/python3
# Copyright: See AUTHORS and COPYING

from sys import *
import struct
import os

n_bytes_que_leer=12


def comprobar_argumentos():
    if len(argv) !=2:
        print("Numero de argumentos incorrecto")
        exit(1)

def desempaquetar():
    f = open(argv[1], 'rb') 
    while 1:
        datos=f.read(n_bytes_que_leer)
        if len(datos) > 0:
            print("---------------------------------------------------")
            print("> Los datos codificados: "+str(datos)+"\n> Tamaño: "+str(len(datos)))
            datos2=struct.unpack("!2b2ih",datos)
            print("> Los datos descodificados: "+str(datos2)+"\n> Tamaño: "+str(len(datos2)))
            
        else: break
    f.close()
    
    

def main():
    comprobar_argumentos()

    #Comprobar tamaño el tamaño del archivo en bytes y cuantos bytes desempaqueto en cada linea. 
    #Nº de bytes(Nº de entradas): 24(1) 12(2) 8(3) 4(4) posibles.
    print("Tamaño del archivo: "+str(os.path.getsize(argv[1])))
    print("Calcsize: "+str(struct.calcsize("2b")))
    desempaquetar()
   
            
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted.')
        exit(0)

