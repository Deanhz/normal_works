# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 15:50:22 2018

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

#指南上的解法
def isBalance(tree):
    result = {0:True}
    getHeight(tree,result,1)
    return result[0]

def getHeight(tree,result,level):
    if not tree:
        result[0] = True
        return level
    leftH = getHeight(tree.left,result,level+1)
    if not result[0]:
        return
    rightH = getHeight(tree.right,result,level+1)
    if not result[0]:
        return 
    if abs(leftH - rightH) > 1:
        result[0] = False
        return
    return max(leftH,rightH)

#王道书上的解法
def isBalance2(tree):
    if not tree:
        return True
    result = {0:True,1:1}
    judge(tree,result)
    return result[0]

def judge(tree,result):
    if not tree:
        result[0] = True
        result[1] = 0
        return
    if not tree.left or not tree.right:
        result[0] = True
        result[1] = 1
    judge(tree.left,result)
    if not result[0]:
        result[0] = False
        return 
    leftH = result[1]
    
    judge(tree.right,result)
    if not result[0]:
        result[0] = False
        return 
    rightH = result[1]
    result[1] = max(leftH,rightH) + 1
    if abs(leftH - rightH) > 1:
        result[0] = False
        return
    result[0] = True
    
    

if __name__ == "__main__":
    preOrder = [1,2,4,8,5,3]
    InOrder = [8,4,2,5,1,3]
    t1 = createByPreInOder(preOrder,InOrder)

    preOrder = [1,2,4,8,5,3,6,7]
    InOrder = [8,4,2,5,1,6,3,7]
    t2 = createByPreInOder(preOrder,InOrder)
    
    print(isBalance(t1))
    print(isBalance(t2))
    print(isBalance2(t1))
    print(isBalance2(t2))











