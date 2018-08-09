# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 19:21:33 2018

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

def preOrderRecur(tree):
    if not tree:
        return
    print(tree.value,end=" ")
    preOrderRecur(tree.left)
    preOrderRecur(tree.right)
    return

def biggestSubBST(tree):
    if not tree:
        return tree
    record = {}
    return posOrder(tree, record)

def posOrder(tree,record):
    if not tree:
        record[0] = 0 #保存最大搜索二叉子树的节点数
        record[1] = float("inf") #保存最小值
        record[2] = -float("inf") #保存最大值
        return None
    lBST = posOrder(tree.left,record)
    lSize = record[0]
    lMin = record[1]
    lMax = record[2]
    rBST = posOrder(tree.right,record)
    rSize = record[0]
    rMin = record[1]
    rMax = record[2]
    record[1] = min(tree.value,lMin)
    record[2] = max(tree.value,rMax)
    if(lBST == tree.left and rBST == tree.right and lMax < tree.value and rMin > tree.value):
        record[0] = lSize + rSize +1
        return tree
    record[0] = max(lSize,rSize)
    if lSize > rSize:
        return lBST
    else:
        return rBST
    
if __name__ == "__main__":
    preOrder = [6,1,0,3,12,10,4,2,5,14,11,15,13,20,16]
    InOrder = [0,1,3,6,2,4,5,10,11,14,15,12,20,13,16]
    tree = createByPreInOder(preOrder,InOrder)
    bigSub1 = biggestSubBST(tree)
    preOrderRecur(bigSub1)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    