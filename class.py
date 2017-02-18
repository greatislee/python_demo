#!/usr/bin/env python
# coding=utf-8



#加了 __变量  就是私有的成员

class Student:
    '''
    学生类
    '''
    def __init__(self,name,age):
        '''
        构造函数
        '''
        print "__init__"
        self.name = name
        self.__age = age
    #加了slef才是类的成员函数
    def showMe(self):
        '''
        普通成员函数
        '''
        print "调用showMe"
        print self.name
        print self.__age

    def __del__(self):
        '''
        析构函数
        '''
        print "__del__"

if __name__ == "__main__":
    s = Student("sf",199)
    s.showMe()

    s.name = "Lina"
    #  私有的age成员不会被改变  但是由于是弱语言 也不会报错，但是不会赋值成功
    s._age = "188"
    s.showMe()




