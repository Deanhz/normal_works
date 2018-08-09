# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 09:10:12 2018

@author: Dean
"""
from collections import Generator,Iterator

def repeater(value):
    while True:
        new = yield value
        if new is not None:
            value = new
            

r = repeater(42)
print(next(r))
print(r.send("hello"))