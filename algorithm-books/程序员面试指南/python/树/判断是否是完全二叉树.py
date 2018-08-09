# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 16:52:31 2018

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

def isCBT(tree):
    if not tree:
        return True
    Q = []
    Q.append(tree)
    while(Q):
        node = Q.pop(0)
        if node:
            Q.append(node.left)
            Q.append(node.right)
        else:
            while(Q):
                tmp = Q.pop(0)
                if tmp:
                    return False
    return True
            
            
  
if __name__ == "__main__":
    preOrder = [1,2,4,5,3,6]
    InOrder = [4,2,5,1,6,3]
    preOrder2 = [1,2,4,5,3,6]
    InOrder2 = [4,2,5,1,3,6]
    tree = createByPreInOder(preOrder,InOrder)
    tree2 = createByPreInOder(preOrder2,InOrder2)
    print(isCBT(tree))
    print(isCBT(tree2))


        
        
        
        
    