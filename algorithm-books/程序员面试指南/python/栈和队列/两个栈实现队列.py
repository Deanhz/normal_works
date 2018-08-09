# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 09:37:24 2018

@author: Dean
"""

class TwoStackQueue(object):
    stackPush = []
    stackPop = []
    
    def add(self, newNum):
        self.stackPush.append(newNum)
    
    def poll(self):
        if not self.stackPush and not self.stackPop:
            raise Exception("queue is empty")
        elif not self.stackPop:
            while self.stackPush:
                self.stackPop.append(self.stackPush.pop())
        return self.stackPop.pop()
    
    def peek(self):
        if not self.stackPush and not self.stackPop:
            raise Exception("queue is empty")
        elif not self.stackPop:
            while self.stackPush:
               self.stackPop.append(self.stackPush.pop())
        return self.stackPop[-1]
    

if __name__ == "__main__":
    s = TwoStackQueue()
    for i in range(5):
        s.add(i)
    print(s.peek())