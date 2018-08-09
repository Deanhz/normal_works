# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 14:42:39 2018

@author: Dean
"""

class Node:
    def __init__(self,value=None):
        self.value = value
        self.left = None
        self.right = None

def createByPreInOder(preOrder,InOrder):
    if not preOrder or not InOrder:
        return None
    length = len(preOrder)
    tree = Node(preOrder[0])
    mid = 0
    for i in range(length):
        if InOrder[i] == preOrder[0]:
            mid = i
            break
    lenL = mid
    tree.left = createByPreInOder(preOrder[1:lenL+1],InOrder[:mid])
    tree.right = createByPreInOder(preOrder[lenL+1:],InOrder[mid+1:])
    return tree
#时间复杂度O(N*M)
def isContains(t1,t2):
    if not t1 and t2:
        return False
    if not t1 and not t2:
        return True
    return check(t1,t2) or isContains(t1.left,t2) or isContains(t1.right,t2)

def check(h,t2):
    if not t2:
        return True
    if not h or h.value != t2.value:
        return False
    return check(h.left,t2.left) and check(h.right,t2.right)

if __name__ == "__main__":
    preOrder = [1,2,4,8,9,5,10,3,6,7]
    InOrder = [8,4,9,2,10,5,1,6,3,7]
    tree = createByPreInOder(preOrder,InOrder)
    preOrder2 = [2,4,8,5]
    InOrder2 = [8,4,2,5]
    tree2 = createByPreInOder(preOrder2,InOrder2)
    print(isContains(tree,tree2))
    
    
    
    
    