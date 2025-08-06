#!/usr/bin/env python3

import socket

client = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8080
try:
    client.connect ((host, port)) # connect to our client
    msg = client.recv (1024)
    client.close()
    print (msg.decode('ascii'))
except ConnectionRefusedError:
    print ("Server did not accept our request for connection!")
    exit (1)
print ("If you see this, it means the except block was not executed.")