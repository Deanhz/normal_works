# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 15:28:08 2018

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

def numTrees(n):
    if n < 2:
        return 1
    num = [0]*(n+1) #num[i]表示i个节点的搜索二叉树有多少种可能
    num[0] = 1
    num[1] = 1
    for i in range(2,n+1): #i为节点总数
        for j in range(1,i+1): #以j为头结点的可能结构有num[i-1]*num[i-j]种
            num[i] += num[j-1]*num[i-j]
    return num[n]

if __name__ == "__main__":
    print(numTrees(2))