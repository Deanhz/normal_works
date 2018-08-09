# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 16:55:22 2018

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
def preOrderRecur(tree):
    if not tree:
        return
    print(tree.value,end=" ")
    preOrderRecur(tree.left)
    preOrderRecur(tree.right)
    return
def posOrderRecur(tree):
    if not tree:
        return
    posOrderRecur(tree.left)
    posOrderRecur(tree.right)
    print(tree.value,end=" ")
    return


def getMaxLen(tree, k):
    if not tree:
        return 0
    dic = {0:0}
    return preOrderMaxLen(tree,k,dic,level=1,maxLen=0,preSum=0)

def preOrderMaxLen(tree,k,dic,level,maxLen,preSum):
    if not tree:
        return maxLen
    curSum = preSum +tree.value
    if curSum not in dic: #这里注意条件！
        dic[curSum] = level
    if (curSum - k) in dic:
        maxLen = max(maxLen,level - dic[curSum - k])
    leftMaxLen = preOrderMaxLen(tree.left,k,dic,level+1,maxLen,curSum)
    rightMaxLen = preOrderMaxLen(tree.right,k,dic,level+1,maxLen,curSum)
    if(dic.get(curSum) == level):
        del(dic[curSum])
    return max(maxLen,leftMaxLen,rightMaxLen)

if __name__ == "__main__":
    preOrder = [-3,3,1,0,-1,6,4,2,5]
    InOrder = [1,3,-1,0,6,-3,2,4,5]
    tree = createByPreInOder(preOrder,InOrder)
    print(getMaxLen(tree,6))
    posOrderRecur(tree)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



    
    
    