# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 20:26:37 2018

@author: Dean
王道p133
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

def IsSimilar(tree1,tree2):
    if not tree1 and not tree2:
        return True
    if not tree1 or not tree2:
        return False
    left = IsSimilar(tree1.left,tree2.left)
    right = IsSimilar(tree1.right,tree2.right)
    if left and right:
        return True
    else:
        return False

if __name__ == "__main__":
    preOrder = [1,2,4,8,9,5,3,6,7]
    InOrder = [8,4,9,2,5,1,6,3,7]
    tree1 = createByPreInOder(preOrder,InOrder)
    tree2 = createByPreInOder(preOrder,InOrder)
    print(IsSimilar(tree1,tree2))
    
    
    