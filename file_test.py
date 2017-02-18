#!/usr/bin/env python
# coding=utf-8


'''
fp = open("./Hero/Es.txt","w")

fp.write("别慌，跳刀还有500块就拿到了，我去打个野\nSF你可以帮我拉个野嘛")

fp.flush()

fp.close()
'''



'''
fp = open("./Hero/Es.txt","r")

mybuf = fp.read()

print mybuf

fp.close()
'''

fp1 = open("./Hero/Es.txt","r")
fp2 = open("./Hero/SF.txt","w")

while True:
    buf = fp1.read()
    if buf == '':
        break
    fp2.write(buf)


fp1.close()
fp2.close()


