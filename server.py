#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" A implementação da aplicação será baseada nos códigos do projeto, Conversão de expressões, desenvolvido na disciplina Programação e Estruturas de Dados do curso de redes de computados do IFPB.
    
    Versão do Python em que foi testada: 3.6
        
    Servidor:
    Após a execução da aplicação o servidor ficará em listen aguardando solicitações de clientes.
    
    1. Após a conexão do cliente, o servidor receberá a (1)Expressão Infixa e o (2)Nome do método para converter (prefixa ou posfixa)
	
    2. Caso a solicitação seja “posfixa”, o servidor converterá a expressão infixa recebida em uma expressão posfixa e enviará ao cliente.
	
    3. Caso a solicitação seja “prefixa”, o servidor converterá a expressão infixa recebida em uma expressão prefixa e enviará ao cliente.
	
    4. Caso a solicitação seja “exit”, o servidor fechará seu lado de conexão com o cliente.
	
    O servidor continuará em listen, aguardando novas conexões, até que se encerre a aplicação com Ctrl + z.
"""

import socket
import os
from ClasseExpressao import *

HOST = '0.0.0.0' # Any network interface available
PORT = 65432 # Port to listen on (non-privileged ports are > 1023)

try:
    tcp=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.bind((HOST, PORT))
    tcp.listen(1)
    print ("[*] Servidor escutando ...")
    print("Pid Principal:",os.getpid())

    while True:
        conn, addr = tcp.accept()
        newpid=os.fork() #clona o processo pai, cria um pid novo para o processo clonado
        print("Processo filho:", newpid)
        if(newpid == 0):
            tcp.close()
            print("Conectado pelo cliente: ",addr)
            while True:
                data1 = conn.recv(1024) # Primeiro dado recebido, expressão infixa 
                dado = data1.decode()
                if (dado=='exit' or dado==''):
                    print("Fechada a conexão com o cliente; ",addr)
                    conn.close()
                    os._exit(0)
                else:
                    exp=Expressao(dado)
                    
                data2 = conn.recv(1024) # Segundo dado recebido, o método
                metodo = data2.decode().upper()
                if(metodo=="POSFIXA"):
                    ExpConvertida=exp.posFixa()
                    conn.sendall(ExpConvertida.encode()) # Envia dado Posfixa para o cliente
                if(metodo=="PREFIXA"):
                    ExpConvertida=exp.preFixa()
                    conn.sendall(ExpConvertida.encode()) # Envia dado Prefixa para o cliente
        else:
            conn.close()
except KeyboardInterrupt:
    print(" Aplicação Servidor encerrada...")
except:
    print(" Problema na aplicação Servidor")