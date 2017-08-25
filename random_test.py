#!/usr/bin/env python
# coding=utf-8

import string,random


data = string.letters+string.digits

def getSubKey():

     return  "".join(random.sample(data,4))

def getKey():
    #  key =[]
    #  for i in range(4):
        #  key.append(getSubKey())

    #  return "-".join(key)
    return "-".join([getSubKey()for i in range(4)])

def getSomeKey(num):
    return [getKey()for i in range(num)]


if __name__ == "__main__":
    print getSomeKey(3)
