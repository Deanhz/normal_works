# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 22:15:28 2018

@author: Dean
"""

class Decorator(object):
    def __init__(self, f):
        self.f = f
    def __call__(self):
        print("decorator start")
        self.f()
        print("decorator end")

@Decorator
def func():
    print("func")

#func()

