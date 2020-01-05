#!/usr/bin/env python3

import socket
import sys

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432  # The port used by the server

if len(sys.argv) > 1:
    HOST = sys.argv[1]
print("Host:", HOST)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        print("-------------------------------")
        try:
           msg = input("Expressão inFixa: ");
        except: break
        s.sendall(str.encode(msg))
        
        try:
            formato=input("preFixa ou posFixa or exit: ")
        except: break
        s.sendall(str.encode(formato))

        data = s.recv(1024)
        dados=data.decode()
        print("Expressão Modificada: ",dados)
