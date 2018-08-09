# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 22:51:39 2018

@author: Dean
"""
class Student:
    def __init__(self, birth):
        self._birth = birth
    def get_birth(self):
        return self._birth
    
    def set_birth(self, value):
        if value <= 2018:
            self._birth = value
    
    birth = property(fget=get_birth, fset=set_birth)
    def get_age(self):
        return 2018 - self._birth
    age = property(fget=get_age)
    
    
s = Student(1994)
print(s.birth)
print(s.age)
s.birth = 2000
print(s.birth)
print(s.age)

s.birth2 = 2019
print(s.birth)
print(s.age)
