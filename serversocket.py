#!/usr/bin/env python
# coding=utf-8


from socket import *
from time import ctime

HOST = '172.27.42.200'
PORT = 20000
BUFSIZE  = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)

tcpSerSock.bind(ADDR)

tcpSerSock.listen(5)

while True:
    print ("waiting for connection...")
    tcpCliSock,addr = tcpSerSock.accept()
    print ("...connected from : ",addr)

    while True:
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
            break
        print("clinet: %s . " % data) 
        SendData = raw_input()
        tcpCliSock.send('[%s] %s' % (ctime(),SendData))

tcpCliSock.close()

tcpSerSock.close()

