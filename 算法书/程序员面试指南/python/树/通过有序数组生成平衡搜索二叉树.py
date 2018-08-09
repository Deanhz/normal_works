# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 17:08:48 2018

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
def inOrderRecur(tree):
    if not tree:
        return
    inOrderRecur(tree.left)
    print(tree.value,end=" ")
    inOrderRecur(tree.right)
    return

def generateBBT(arr):
    if not arr:
        return arr
    tree = BBT(arr)
    return tree

def BBT(arr):
    if not arr:
        return None
    length = len(arr)
    mid = length // 2
    node = Node(arr[mid])
    node.left = BBT(arr[:mid])
    node.right = BBT(arr[mid+1:])
    return node

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8]
    tree = generateBBT(arr)
    preOrderRecur(tree)
    print()
    inOrderRecur(tree)
    
    
    
    
    
    
    