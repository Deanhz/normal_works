# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 10:10:20 2018

@author: Dean
"""

class MyClass:
    def __init__(self,value):
        self.name = value
    def func(self):
        pass
    @staticmethod
    def static_method(self):
        print("static method")
    @classmethod
    def class_method(cls,name):
        obj = cls(name)
        print("class method of ",cls)
        return obj
        

print(type(MyClass.func))
print(type(MyClass.static_method))
print(type(MyClass.class_method))
print()
print(type(MyClass("my").func))
print(type(MyClass("my").static_method))
print(type(MyClass("my").class_method))

obj = MyClass.class_method("dean")
print(obj.name)