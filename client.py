#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" A implementação da aplicação será baseada nos códigos do projeto, Conversão de expressões, desenvolvido na disciplina Programação e Estruturas de Dados do curso de redes de computados do IFPB.

    Versão do Python em que foi testada: 3.6

    Cliente:
	Após a execução da aplicação cliente, será iniciada uma conexão com o servidor, em seguida será solicitado ao usuário a digitação de uma expressão infixa.
        exemplo: A + B * C
	
    1. O comando “posfixa” solicitará ao servidor a conversão da expressão infixa anteriormente digitada em uma expressão posfixa, mostrando a conversão em tela do cliente.
        exemplo: A B C * +
	
    2. O comando “prefixa” solicitará ao servidor a conversão da expressão infixa anteriormente digitada em uma expressão prefixa, mostrando a conversão em tela do cliente.
        exemplo: + A * B C
	
    3. A opção “exit” fecha a conexão do lado cliente da aplicação.
"""

import socket
import sys

HOST = 'localhost'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

if len(sys.argv) > 1:
    HOST = sys.argv[1]

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("Conectado ao Servidor:", HOST)
        while True:
            try:
                print("\nConversor de Expressões Infixa")
                print("=-="* 10)
                print("Expressão Infixa \t1")
                print("Exit             \t2")
                print("=-="* 10)
                op = input (">>>> Opção: ")
                assert op=="1" or op=="2"
            
                if (op == "1"):
                    msg = input("\nDigite a Expressão InFixa: ")            
                    s.sendall(str.encode(msg))
                
                    formato=input("preFixa ou posFixa: ")
                    s.sendall(str.encode(formato))
                
                    data = s.recv(1024)
                    dados=data.decode()
                    print("Expressão Modificada: ",dados)
                elif (op == "2"):
                    s.close()
                    break
            except AssertionError:
                print('\nOpção inválida. Tente uma opção do menu!')

except KeyboardInterrupt:
    print(" Aplicação cliente fechada!")
except:
    print(" Servidor indisponível no momento. Por favor tente mais tarde.")
