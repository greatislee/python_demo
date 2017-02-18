#!/usr/bin/env python
# coding=utf-8




# 会将去不不定长参数放在一个元祖中  一个*
def func(a,*args):
    print a
    print "-"*10
    print args

#会将全部不定长参数放在一个字典中  两个*
def func2(a,**args):
    print a
    print "-"*10
    print args

func (1,2,3,4,45,5,6)

print "+"*10

func2(10,name="lee",age=16,sex='man')

