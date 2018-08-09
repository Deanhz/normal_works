# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 09:33:15 2018

@author: Dean
"""
node = None

class Node:
    def __init__(self,value=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

def createByPreInOder(preOrder,InOrder):
    global node
    if not preOrder or not InOrder:
        return None
    length = len(preOrder)
    tree = Node(preOrder[0])
    if preOrder[0] == 5:
        node = tree
    mid = 0
    for i in range(length):
        if InOrder[i] == preOrder[0]:
            mid = i
            break
    lenL = mid
    tree.left = createByPreInOder(preOrder[1:lenL+1],InOrder[:mid])
    if tree.left:
        tree.left.parent = tree
    tree.right = createByPreInOder(preOrder[lenL+1:],InOrder[mid+1:])
    if tree.right:
        tree.right.parent = tree
    return tree

def getNextNode(p):
    if p.right:
        return p.right.value
    parent = p.parent
    if parent.left == p:
        return parent.value
    flag = True
    q = None
    while(flag):
        q = parent
        parent = parent.parent
        if not parent:
            return None
        if parent.left == q:
            return parent.value
        
if __name__ == "__main__":
    preOrder = [1,2,4,5,3,6,7,8]
    InOrder = [4,2,5,1,6,3,8,7]
    tree = createByPreInOder(preOrder,InOrder)
    print(getNextNode(node))
    
        
        
        
        
        
        
        
    
