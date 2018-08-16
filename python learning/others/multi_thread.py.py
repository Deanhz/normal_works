# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 14:36:55 2018

@author: Dean
"""

from threading import Thread
import time

def my_counter():
    i = 0
    for _ in range(100000000):
        i = i + 1
    return True

def main():
    thread_array = {}
    start_time = time.time()
    for tid in range(2):
        t = Thread(target=my_counter)
        t.start()
        thread_array[tid] = t
    for i in range(2):
        thread_array[i].join()
    end_time = time.time()
    print("multi thread Total time: {}".format(end_time - start_time))

if __name__ == '__main__':
    main()