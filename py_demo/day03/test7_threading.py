#coding:utf-8

import threading
import time


def active(*args):
    time.sleep(args[0])
    print "active theading " + str(args)


if __name__=="__main__":

    thread_list = []

    t1 = threading.Thread(target=active, args=(2, ), )
    t2 = threading.Thread(target=active, args=(3, ))

    thread_list.append(t1)
    thread_list.append(t2)

    t1.start()
    t2.start()

    for thread in thread_list:
        thread.join()
        print "joind"


