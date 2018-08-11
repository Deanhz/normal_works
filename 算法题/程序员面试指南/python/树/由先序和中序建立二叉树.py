# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 20:46:46 2018

@author: Dean
"""

class Node:
    def __init__(self,value=None):
        self.value = value
        self.left = None
        self.right = None
def preOrderRecur(tree):
    if not tree:
        return
    print(tree.value,end=" ")
    preOrderRecur(tree.left)
    preOrderRecur(tree.right)
    return

def inOrderRecur(tree):
    if not tree:
        return
    inOrderRecur(tree.left)
    print(tree.value,end=" ")
    inOrderRecur(tree.right)
    return

def posOrderRecur(tree):
    if not tree:
        return
    posOrderRecur(tree.left)
    posOrderRecur(tree.right)
    print(tree.value,end=" ")
    return
############################################################################

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



if __name__ == "__main__":
    preOrder = [1,2,4,8,9,5,1,6,7]
    InOrder = [8,4,9,2,5,1,6,1,7]
    tree = createByPreInOder(preOrder,InOrder)
    preOrderRecur(tree)
    print()
    inOrderRecur(tree)
    print()
    posOrderRecur(tree)
    
    