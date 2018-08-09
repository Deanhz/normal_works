# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 15:19:22 2018

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

def levelPrint(tree):
    if not tree:
        return tree
    queue = []
    queue.append(tree)
    tmp = []
    last = tree
    level = 1
    while(queue):
        node = queue.pop(0)
        tmp.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        if node == last:
            print("level {} :".format(level),end=" ")
            for i in tmp:
                print(i.value,end=" ")
            print()
            tmp = []
            level += 1
            last = queue[-1] if queue else None

def ZigZag(tree):
    if not tree:
        return tree
    queue = []
    queue.append(tree)
    tmp = []
    last = tree
    level = 1
    k = 0
    while(queue):
        node = queue.pop(0)
        tmp.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        if node == last:
            if k%2 == 0:
                print("level {} from left to right:".format(level),end=" ")
                for i in tmp:
                    print(i.value,end=" ")
            else:
                print("level {} from right to left:".format(level),end=" ")
                for i in tmp[::-1]:
                    print(i.value,end=" ")
            print()
            tmp = []
            level += 1
            k += 1
            last = queue[-1] if queue else None

if __name__ == "__main__":
    preOrder = [1,2,4,3,5,7,8,6]
    InOrder = [4,2,1,7,5,8,3,6]
    tree = createByPreInOder(preOrder,InOrder)
    levelPrint(tree)
    ZigZag(tree)
    
        