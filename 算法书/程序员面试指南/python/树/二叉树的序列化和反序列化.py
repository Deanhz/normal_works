# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 10:49:56 2018

@author: Dean
"""

#通过先序遍历实现序列化和反序列化
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

def serialByPre(tree):#先序实现序列化，空用#表示，每个值后面都加“!”来分割。
    if(not tree):
        return "#!"
    val = str(tree.value) + "!"
    leftVal = serialByPre(tree.left)
    rightVal = serialByPre(tree.right)
    return val+leftVal+rightVal

def reconByPreString(preStr):
    if not preStr:
        return None
    values = preStr.split("!")
    return reconPreOrder(values)

def reconPreOrder(values):
    val = values.pop(0)
    if val == "#":
        return None
    node = Node(val)
    node.left = reconPreOrder(values)
    node.right = reconPreOrder(values)
    return node
    
    
    
if __name__ == "__main__":
    preOrder = [1,2,4,8,9,5,3,6,7]
    InOrder = [8,4,9,2,5,1,6,3,7]
    tree = createByPreInOder(preOrder,InOrder)
    preOrderRecur(tree)
    print()
    result = serialByPre(tree)
    print(result)
    tree2 = reconByPreString(result)
    preOrderRecur(tree2)