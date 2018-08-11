# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 19:23:12 2018

@author: Dean
王道
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

def BtWith(tree):
    if not tree:
        return 0
    Q = []
    data = []
    tmp = []
    level = 0
    last = tree
    Q.append(tree)
    while(Q):
        node = Q.pop(0)
        tmp.append(node.value)
        if node.left:
            Q.append(node.left)
        if node.right:
            Q.append(node.right)
        if last == node:
            last = Q[-1] if Q else None
            level += 1
            data.append(tmp)
            tmp = []        
    level_n_max = 0
    for i in data:
        if len(i) > level_n_max:
            level_n_max = len(i)
    return level_n_max
    

    
if __name__ == "__main__":
    preOrder = [1,2,4,8,9,5,3,6,7]
    InOrder = [8,4,9,2,5,1,6,3,7]
    tree = createByPreInOder(preOrder,InOrder)
    print(BtWith(tree))
    
    
    
    
    
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
