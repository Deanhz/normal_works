# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 09:18:48 2018

@author: Dean
"""

class NewStack1:
    def __init__(self):
        self.stackData = []
        self.stackMin = []
    
    def push(self, newNum):
        self.stackData.append(newNum)
        if len(self.stackMin) == 0 or newNum <= self.getMin():
            self.stackMin.append(newNum)
    
    def pop(self):
        if len(self.stackData) == 0:
            raise Exception("stack is empty")
        value = self.stackData.pop()
        if self.getMin() == value:
            self.stackMin.pop()
        return value
    
    def getMin(self):
        if len(self.stackMin) == 0:
            raise Exception("stack is empty")
        return self.stackMin[-1]