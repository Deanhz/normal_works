# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 16:03:33 2018

@author: Dean
面试指南P178
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

def preOrderTravel(tree):#最基本的做法，时间复杂度O(N)
    if not tree:
        return 0
    leftN = preOrderTravel(tree.left)
    rightN = preOrderTravel(tree.right)   
    return leftN + rightN + 1

#该解法时间复杂度为O(h^2)，具体过程参考面试指南
def nodeNum(head):
    if not head:
        return 0
    return bs(head,1,mosLeftLevel(head,1))

def mosLeftLevel(n,level):#求以n为头结点的完全二叉树的最大层数。
    while(n):
        level += 1
        n = n.left
    return level - 1

def bs(head,l,h): #返回以head为头结点的完全二叉树的节点数。l表示head所在层次，h为树的层数(始终不变).
    if l == h:
        return 1
    if(mosLeftLevel(head.right,l+1) == h):
        return 2**(h-l) + bs(head.right,l+1,h)
    else:
        return 2**(h-l-1) + bs(head.left,l+1,h)
    
    
    
if __name__ == "__main__":
    preOrder = [1,2,4,5,3,6,7]
    InOrder = [4,2,5,1,6,3,7]
    posOrder = [4,5,2,6,7,3,1]
    tree = createByPreInOder(preOrder,InOrder)
    print(preOrderTravel(tree))
    print(nodeNum(tree))
        
        
        
        
        
        