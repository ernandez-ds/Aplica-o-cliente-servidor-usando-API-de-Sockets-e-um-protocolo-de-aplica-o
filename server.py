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
	
    O servidor continuará em listen, aguardando novas conexões, até que se encerre a aplicação com Ctrl + c.
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
            print("Conectado pelo cliente:",addr)
            while True:
                msg1 = conn.recv(1024) # Primeira mensagem recebida, expressão infixa 
                dado = msg1.decode()
                print("Cliente:",addr,", mensagem-1:",dado) ### Exibindo mensagem-1 do cliente
                if (dado=='exit'):
                    print("Fechada a conexão com o cliente:",addr)
                    conn.close()
                    os._exit(0)
                else:
                    exp=Expressao(dado)
                                        
                msg2 = conn.recv(1024) # Segunda mensagem recebida, o método
                metodo = msg2.decode().lower()
                print("Cliente:",addr,", mensagem-2:",metodo) ### Exibindo mensagem-2 do cliente
                if(metodo=="posfixa"):
                    ExpConvertida=exp.posFixa()
                    conn.send(ExpConvertida.encode()) # Envia dado Posfixa para o cliente
                if(metodo=="prefixa"):
                    ExpConvertida=exp.preFixa()
                    conn.send(ExpConvertida.encode()) # Envia dado Prefixa para o cliente
                
                print("Servidor ao Cliente:",addr,", mensagem-3:",ExpConvertida) ### Exibindo mensagem-3 do Servidor
        else:
            conn.close()
except KeyboardInterrupt:
    print(" Aplicação Servidor encerrada...")
except:
    print(" Problema na aplicação Servidor")