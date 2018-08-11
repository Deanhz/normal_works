# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 20:13:39 2018

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

def treeLinkList(tree):
    if not tree:
        return None
    head = None
    pre = None
    def preOrder(tree):
        nonlocal head
        nonlocal pre
        if not tree:
            return
        if not tree.left and not tree.right:
            if pre == None:
                head = tree
                pre = tree
            else:
                pre.right = tree
                pre = tree
        preOrder(tree.left)
        preOrder(tree.right)
        pre.right = None
    preOrder(tree)
    return head

if __name__ == "__main__":
    preOrder = [1,2,4,8,9,5,3,6,7]
    InOrder = [8,4,9,2,5,1,6,3,7]
    tree = createByPreInOder(preOrder,InOrder)
    head = treeLinkList(tree)
    while(head):
       print(head.value)
       head = head.right