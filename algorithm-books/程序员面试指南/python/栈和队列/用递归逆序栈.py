# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 10:22:23 2018

@author: Dean
"""
def getAndRemoveLast(stack):
    result = stack.pop()
    if len(stack) == 0:
        return result
    else:
        i = getAndRemoveLast(stack)
        stack.append(result)
        return i

def reverse(stack):
    if len(stack) == 0:
        return
    i = getAndRemoveLast(stack)
    reverse(stack)
    stack.append(i)
    return stack

if __name__ == "__main__":
    s = []
    for i in range(5):
        s.append(i)
    print(s)
    print(reverse(s))
    