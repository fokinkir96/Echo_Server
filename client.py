#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
sock.send('hello, world!'.encode('UTF-8'))

data = sock.recv(1024)
sock.close()

print(data)