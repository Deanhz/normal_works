# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 19:30:13 2018

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
    lenL = mid
    tree.left = createByPreInOder(preOrder[1:lenL+1],InOrder[:mid])
    tree.right = createByPreInOder(preOrder[lenL+1:],InOrder[mid+1:])
    return tree

def getHeight(tree):
    if not tree:
        return 0
    leftH = getHeight(tree.left)
    rightH = getHeight(tree.right)
    return max(leftH,rightH) + 1

def setEdgeMap(tree,k,edgeMap):#找出左右两侧的边界节点
    if not tree:
        return
    if not edgeMap[k][0]:
        edgeMap[k][0] = tree
    edgeMap[k][1] = tree
    setEdgeMap(tree.left,k+1,edgeMap)
    setEdgeMap(tree.right,k+1,edgeMap)
    return
    
def printLeafNotInMap(tree,k,edgeMap):#找到下方的边界节点
    if not tree:
        return
    if(not tree.left and not tree.right and tree!=edgeMap[k][0] and tree!=edgeMap[k][1]):
        print(tree.value,end=" ")
    printLeafNotInMap(tree.left,k+1,edgeMap)
    printLeafNotInMap(tree.right,k+1,edgeMap)
    return

def printEdge1(tree):
    if not tree:
        return tree
    height = getHeight(tree)
    edgeMap = [[None for i in range(2)] for j in range(height)]
    setEdgeMap(tree,0,edgeMap)
    for i in range(0,len(edgeMap)):#打印左侧边界节点
        print(edgeMap[i][0].value,end=" ")
    printLeafNotInMap(tree,0,edgeMap)#打印下方边界节点
    for i in range(0,len(edgeMap))[::-1]:#打印右侧边界节点
        print(edgeMap[i][1].value,end=" ")
        
    
    


if __name__ == "__main__":
    pre = [1,2,4,7,8,11,13,14,3,5,9,12,15,16,10,6]
    In = [2,7,4,8,13,11,14,1,15,12,16,9,5,10,3,6]
    tree = createByPreInOder(pre,In)
    printEdge1(tree)



















