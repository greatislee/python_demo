#!/usr/bin/env python
# coding=utf-8




#外部函数

def counter():
    count = [0]

    #内部函数
    def incr():
        count[0] = count[0] + 1
        return count[0]

    return incr



