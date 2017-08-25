#!/usr/bin/env python
# coding=utf-8

from socket import *

HOST = '172.27.42.200'
PORT = 20000
BUFSIZE  = 1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = raw_input('> ')
    if not data:
        print ("input is not null!!")
        continue
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print (data)

tcpCliSock.close()
