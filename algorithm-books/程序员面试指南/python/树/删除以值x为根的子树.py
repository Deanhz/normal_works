# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 14:35:21 2018

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
def preOrderUnRecur(tree):
    if not tree:
        return 
    stack = []
    stack.append(tree)
    while(stack):
        node = stack.pop()
        print(node.value,end=" ")
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    print()
    return


#删除函数
def DeleteTree(tree):
    if not tree:
        return
    DeleteTree(tree.left)
    DeleteTree(tree.right)
    del(tree)
    return

def search_deleteX(tree,x):
    if not tree:
        return None
    leftValue = search_deleteX(tree.left,x)
    if leftValue == x:
        DeleteTree(tree.left)
        tree.left = None
    rightValue = search_deleteX(tree.right,x)
    if rightValue == x:
        DeleteTree(tree.right)
        tree.right = None
    return tree.value
    
if __name__ == "__main__":
    preOrder = [1,2,4,8,5,3,6,7]
    InOrder = [8,4,2,5,1,6,3,7]
    tree = createByPreInOder(preOrder,InOrder)
    preOrderUnRecur(tree)
    search_deleteX(tree,4)
    preOrderUnRecur(tree)
    
        