#!/usr/bin/env python3
# Echo client program
import socket

HOST = 'bsd5.cs.nctu.edu.tw'    # The remote host
PORT = 50007              # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(b'Hello, world')

data = s.recv(1024)
s.close()
print('Received', repr(data))

