# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 09:28:41 2018

@author: Dean
"""

class Node:
    def __init__(self,value=None):
        self.value = value
        self.left = None
        self.right = None
        
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

def posOrderRecur(tree):
    if not tree:
        return
    posOrderRecur(tree.left)
    posOrderRecur(tree.right)
    print(tree.value,end=" ")
    return


def createByPreAndIn(preArr,InArr):
    if not preArr or not InArr:
        return None
    rootValue = preArr[0]
    mid = 0
    for i in InArr:
        if i == rootValue:
            break
        mid += 1
    Llen = len(InArr[:mid])
    Rlen = len(InArr[mid+1:])
    root = Node(rootValue)
    root.left = createByPreAndIn(preArr[1:Llen+1],InArr[:mid])
    root.right = createByPreAndIn(preArr[Llen+1:],InArr[mid+1:])
    return root

def createByInAndPos(InArr,posArr):
    if not InArr or not posArr:
        return None
    mid = 0
    for i in InArr:
        if i == posArr[-1]:
            break
        mid += 1
    root = Node(posArr[-1])
    Llen = mid
    root.left = createByInAndPos(InArr[:mid],posArr[:Llen])
    root.right = createByInAndPos(InArr[mid+1:],posArr[Llen:-1])
    return root

#注意只有不存在度为1的节点的二叉树才能被先序和后序重构
def createByPreAndPos(preArr,posArr):
    if not preArr and not posArr:
        return None
    root = Node(preArr[0])
    k = 0
    leftRoot = None #左子树的根节点
    if len(preArr) > 1: #这个地方要注意，需要特殊处理，负责就报错了。
        leftRoot = preArr[1]
    for i in posArr:
        if i == leftRoot:
            break
        k += 1
    Llen = 0
    if leftRoot is not None: #同理，这个地方要特殊处理。
        Llen = k + 1 #求出左子树包含的节点数
    root.left = createByPreAndPos(preArr[1:Llen+1],posArr[:Llen])
    root.right = createByPreAndPos(preArr[Llen+1:],posArr[Llen:-1])
    return root
    
    

if __name__ == "__main__":
    preOrder = [1,2,4,5,3,6,7]
    InOrder = [4,2,5,1,6,3,7]
    posOrder = [4,5,2,6,7,3,1]
    tree = createByPreAndIn(preOrder,InOrder)
    tree2 = createByInAndPos(InOrder,posOrder)
    tree3 = createByPreAndPos(preOrder,posOrder)
    preOrderRecur(tree)
    print()
    inOrderRecur(tree)
    print()
    posOrderRecur(tree)
    print()
    preOrderRecur(tree2)
    print()
    inOrderRecur(tree2)
    print()
    posOrderRecur(tree2)
    print()
    preOrderRecur(tree3)
    print()
    inOrderRecur(tree3)
    print()
    posOrderRecur(tree3)
    print()  
    
    
