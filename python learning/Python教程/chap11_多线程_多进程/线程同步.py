# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 15:04:57 2018

@author: user
"""
import threading
import dis


total = 0
lock = threading.Lock()

def add():
    global total
    for i in range(1000000):
        lock.acquire()
        total += 1
        lock.release()
    
def desc():
    global total
    for i in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()

if __name__ == "__main__":
    t1 = threading.Thread(target=add)
    t2 = threading.Thread(target=desc)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(total)
