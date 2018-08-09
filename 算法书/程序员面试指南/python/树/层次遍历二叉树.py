# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 19:54:40 2018

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

def levelTrave(tree):
    if not tree:
        return None
    Q = []
    level = 0
    last = tree
    Q.append(tree)
    while(Q):
        node = Q.pop(0)
        print("level {}:".format(level))
        print(node.value)
        if node.left:
            Q.append(node.left)
        if node.right:
            Q.append(node.right)
        if node == last:
            last = Q[-1] if Q else None
            level += 1
    return

if __name__ == "__main__":
    preOrder = [1,2,4,8,9,5,3,6,7]
    InOrder = [8,4,9,2,5,1,6,3,7]
    tree = createByPreInOder(preOrder,InOrder)
    levelTrave(tree)
        
        
        
        