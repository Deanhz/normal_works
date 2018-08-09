# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 10:47:47 2018

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
def posOrderRecur(tree):
    if not tree:
        return
    posOrderRecur(tree.left)
    posOrderRecur(tree.right)
    print(tree.value,end=" ")
    return

def generatePosOrder(preArr,InArr):#通过先序和中序生成后序数组，不能重建二叉树
    if not preArr or not InArr:
        return preArr
    posArr = []
    generate(preArr,InArr,posArr)
    return posArr[::-1]

def generate(preArr,InArr,posArr):
    if not preArr or not InArr:
        return 
    rootValue = preArr[0]
    mid = 0
    for i in InArr:
        if i == rootValue:
            break
        mid += 1
    posArr.append(rootValue)
    generate(preArr[mid+1:],InArr[mid+1:],posArr)
    generate(preArr[1:mid+1],InArr[:mid],posArr)
    return

if __name__ == "__main__":
    preOrder = [1,2,4,5,3,6,7]
    InOrder = [4,2,5,1,6,3,7]
    posOrder = [4,5,2,6,7,3,1]
    tree = createByPreInOder(preOrder,InOrder)
    posOrderRecur(tree)
    print()
    print()
    print(generatePosOrder(preOrder,InOrder))
    


    

