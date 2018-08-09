# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 10:18:22 2018

@author: Dean
"""

class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print("eating...")
            self.hungry = False
        else:
            print("no thanks")

class SongBird(Bird):
    def __init__(self):
        super().__init__()
        self.type = "SongBird"
    def sing(self):
        print("I am",self.type)
class DanceBird(Bird):
    def __init__(self):
        self.type = "DanceBird"
    

sb = SongBird()
sb.eat()
sb.eat()

