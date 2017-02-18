#!/usr/bin/env python
# coding=utf-8



class Hero:
    '''
    英雄类
    '''
    def __init__(self,name):
        print "Hero.__init__"
        self.name = name

    def show(self):
        print "Hero.showMe"
        print self.name
class agility(Hero):
    '''
    敏捷类
    '''
    def __init__(self,name,speed):
       #调用子类构造 会默认调用父类构造
       #python 需要显示的调用父类的构造
       Hero.__init__(self,name) 
       self.speed= speed
    def show(self):
       print "agility show()" 
       print self.name
       print self.speed

if __name__ == "__main__":
    h = Hero ("Icefrog")
    h.show()
    print "*"*20
    a = agility("Mor",522)
    a.show()
