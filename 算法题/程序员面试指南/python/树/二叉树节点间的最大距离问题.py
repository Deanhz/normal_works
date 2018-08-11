# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 09:15:34 2018

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

def maxDistance(tree):
    if not tree:
        return 0
    record = {}
    return posOrder(tree,record)

def posOrder(head,record):
    if not head:
        record[0] = 0
        return 0
    lMax = posOrder(head.left,record)
    maxFromLeft = record[0]
    rMax = posOrder(head.right,record)
    maxFromRight = record[0]
    curNodeMax = maxFromLeft + maxFromRight + 1
    record[0] = max(maxFromLeft,maxFromRight) + 1
    return max(lMax,rMax,curNodeMax)
    
if __name__ == "__main__":
    preOrder = [1,2,4,5,3,6,7]
    InOrder = [4,2,5,1,6,3,7]
    tree = createByPreInOder(preOrder,InOrder)
    print(maxDistance(tree))
    
    