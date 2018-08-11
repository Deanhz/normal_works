# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 10:23:24 2018

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

def isBSTNode(h,n,value):#判断n节点是否属于h节点的二叉搜索树
    if not h:
        return False
    if h == n:
        return True
    if h.value > value:
        return isBSTNode(h.left,n,value)
    else:
        return isBSTNode(h.right,n,value)

def maxTopo(h,n):#找到属于h节点二叉搜索树的以n节点为根的最大子树。
    if(h and n and isBSTNode(h,n,n.value)):
        return maxTopo(h,n.left) +maxTopo(h,n.right) + 1
    return 0 #返回节点数
def bstTopoSize(tree):
    if not tree:
        return 0
    max_Toposize = maxTopo(tree,tree)
    left_max = bstTopoSize(tree.left)
    right_max = bstTopoSize(tree.right)
    return max(max_Toposize,left_max,right_max)
    

if __name__ == "__main__":
    preOrder = [6,1,0,3,12,10,4,2,5,14,11,15,13,20,16]
    InOrder = [0,1,3,6,2,4,5,10,11,14,15,12,20,13,16]
    tree = createByPreInOder(preOrder,InOrder)
    print(bstTopoSize(tree))
    
    
    
    