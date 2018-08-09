# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 14:12:19 2018

@author: Dean
王道p119:8
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

def countTwo(tree): # by me
    if not tree:
        return 0
    record = {0:0}
    def posOrder(head,record):
        if not head:
            return None
        left = posOrder(head.left, record)
        right = posOrder(head.right, record)
        if left and right:
            record[0] += 1
        return head
    
    posOrder(tree,record)
    return record[0]

def DsonNodes(tree):#王道p128
    if not tree:
        return 0
    if tree.left and tree.right:
        return DsonNodes(tree.left) + DsonNodes(tree.right) + 1
    else:
        return DsonNodes(tree.left) + DsonNodes(tree.right)

if __name__ == "__main__":
    preOrder = [1,2,4,8,5,3,6,7]
    InOrder = [8,4,2,5,1,6,3,7]
    tree = createByPreInOder(preOrder,InOrder)
    print(countTwo(tree))
    print(DsonNodes(tree))
    
    
    
    