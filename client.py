#!/usr/bin/env python3

import socket

client = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8080

client.connect ((host, port)) # connect to our client
msg = client.recv (1024)
client.close()

print (msg.decode('ascii'))