#!/usr/bin/env python
# coding=utf-8





fruit = ["apple","banana","orage",[1,3,4],5,6]


for item in fruit:
    if type(item) == type(9):
        print "int"
    elif type(item) == type(""):
        print "str"
    print item 


for i in range(5):
    print i
