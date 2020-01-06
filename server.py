#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

HOST = '0.0.0.0' # Any network interface available
PORT = 65432 # Port to listen on (non-privileged ports are > 1023)

from ClasseExpressao import *

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        try:
            conn, addr = s.accept()
        except: break
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                expressao=data.decode()
                print ("Primeiro dado cliente:", expressao)
                if not data: break
                exp=Expressao(expressao) # Instanciando um objeto
                    
                data = conn.recv(1024)
                formato=data.decode()
                print("Segundo dados do cliente:", formato)
               
                if(formato=="posFixa"):
                    data=exp.posFixa()
                    conn.sendall(data.encode()) #Enviar dado para o cliente
                if(formato=="preFixa"):
                    data=exp.preFixa()
                    conn.sendall(data.encode()) #Enviar dado para o cliente
