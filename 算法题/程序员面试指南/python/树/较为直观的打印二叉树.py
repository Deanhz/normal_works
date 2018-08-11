# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 20:21:14 2018

@author: Dean
"""

class Node:
    def __init__(self,value=None):
        self.value = value
        self.left = None
        self.right = None

def create(d):
    if not d:
        return None
    data = d.copy()
    bt = Node(data.pop(0))
    R = bt
    while(data):
        left = Node(data.pop(0))
        right = Node(data.pop(0))
        R.left = left
        R.right = right
        R = right
    return bt

def printTree(tree,mark,k):
    if not tree:
        return
    printTree(tree.right,"v",k+1)
    val = mark + str(tree.value) +mark
    lenM = len(val)
    lenL = (17 - lenM) //2
    lenR = 17 - lenM - lenL
    print(" " *k + " "*lenL + val + " "*lenR)
    printTree(tree.left,"^",k+1)
    
if __name__ == "__main__":
    data = [1,2,3,4,5,6,7,8,9]
    tree = create(data)
    printTree(tree,"H",0)
    
