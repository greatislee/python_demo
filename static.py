#!/usr/bin/env python
# coding=utf-8
   



class Hero:
    speed = 522

    def __init__(self,name):
        self.name = name

    def showMe(self):
        print self.name

    @classmethod
    def getSpeed(cls):
        return cls.speed


if __name__ == "__main__":
    h = Hero("xuemo")

    h.showMe()

    print Hero.getSpeed()
