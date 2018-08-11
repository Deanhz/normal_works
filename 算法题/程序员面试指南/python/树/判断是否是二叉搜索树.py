# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 10:41:41 2018

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

def judge1(tree):
    if not tree:
        return True
    def posOrder(tree,record):#后续遍历，先判断左右子树，分别求出左右子树的最大、最小值，再判断当前节点。
        if not tree:
            record[0] = float("inf") #保存最小值
            record[1] = -float("inf") #保存最大值
            return True
        isleft = posOrder(tree.left,record)
        leftMin = record[0]
        leftMax = record[1]
        isright = posOrder(tree.right,record)
        rightMin = record[0]
        rightMax = record[1]
        record[0] = min(tree.value,leftMin,rightMin)
        record[1] = max(tree.value,leftMax,rightMax)
        if(isleft and isright and leftMax < tree.value and tree.value < rightMin):
            return True
        else:
            return False
    record = {}
    return posOrder(tree,record)

def judge2(tree):
    if not tree:
        return True
    lastValue = -float("inf")
    def posOrder(tree):
        if not tree:
            return True
        left = posOrder(tree.left)
        if not left:
            return False
        value = tree.value
        if lastValue > value:
            return False
        lastValue = value
        right = posOrder(tree.left)
        return right
    
    

if __name__ == "__main__":
    preOrder = [6,1,0,3,12,10,4,2,5,14,11,15,13,20,16]
    InOrder = [0,1,3,6,2,4,5,10,11,14,15,12,20,13,16]
    preOrder2 = [10,4,2,5,14,11,15]
    InOrder2 = [2,4,5,10,11,14,15]
    tree = createByPreInOder(preOrder,InOrder)
    tree2 = createByPreInOder(preOrder2,InOrder2)
    print(judge1(tree))
    print(judge1(tree2))

