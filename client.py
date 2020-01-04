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
    #s.sendall(b'Hello, world')
    while True:
        try:
            msg = input("Message: ");
        except: break
        s.sendall(str.encode(msg))
        data = s.recv(1024)
        # EU ALTEREI
        #print("Received", repr(data))
        dados=data.decode()
        print("Received",dados)
