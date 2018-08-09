# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 15:53:15 2018

@author: Dean
p134
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

def getTwoErrNodes(tree):
    if not tree:
        return tree
    errors = {}
    stack = []
    pre = None
    while(stack or tree):
        if tree:
            stack.append(tree)
            tree = tree.left
        else:
            node = stack.pop()
            if(pre and pre.value > node.value):
                if 0 not in errors:
                    errors[0] = pre
                errors[1] = node
            pre = node
            tree = node.right
    return errors

    
    return errors

if __name__ == "__main__":
    preOrder = [4,5,1,3,2]
    InOrder = [1,5,3,4,2]
    preOrder2 = [3,2,1,4,5]
    InOrder2 = [1,2,4,3,5]
    tree = createByPreInOder(preOrder,InOrder)
    tree2 = createByPreInOder(preOrder2,InOrder2)
    errors = getTwoErrNodes(tree)
    errors2 = getTwoErrNodes(tree2)
    print(errors.get(0).value,errors.get(1).value)
    print(errors2.get(0).value,errors2.get(1).value)   