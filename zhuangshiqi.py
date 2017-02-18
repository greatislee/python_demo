#!/usr/bin/env python
# coding=utf-8


#装饰器函数
def doc_func(func):

    #包裹函数（闭包，额外需要添加的功能全部在此函数中添加）
    def warpfunc():
        #做一些额外事情
        print "%s 给你一个刷新球" %(func.__name__)
        func()

    return warpfunc


@doc_func
def sf():
    print "神牛你的F呢"

@doc_func
def es():
    print "F还有5s,CD"


if __name__ == "__main__":
   
    sf()
    es()
