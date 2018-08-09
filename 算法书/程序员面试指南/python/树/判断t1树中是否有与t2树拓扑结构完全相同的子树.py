# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 14:51:10 2018

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

#方法一
#对t1的每颗子树都判断是否与t2的拓扑结构完全一样
#时间复杂度O(M*N)
def isSubTree(t1,t2):
    if not t1 and t2:
        return False
    if not t1 and not t2:
        return True
    return check(t1,t2) or isSubTree(t1.left,t2) or isSubTree(t1.right,t2)

def check(h,t2):
    if not h and not t2:
        return True
    elif h and t2:
        if h.value != t2.value:
            return False
        else:
            return check(h.left,t2.left) and check(h.right,t2.right)
    else:
        return False
    
#方法二
#序列化，再判断t2的序列化结果是否是t1的子串
#时间复杂度O(M+N)
def serializeByPre(tree):
    if not tree:
        return "#!"
    value = str(tree.value) +"!"
    left = serializeByPre(tree.left)
    right = serializeByPre(tree.right)
    return value+left+right

def isSubTree2(t1,t2):
    t1Str = serializeByPre(t1)
    t2Str = serializeByPre(t2)
    if t2Str in t1Str:
        return True
    else:
        return False


if __name__ == "__main__":
    preOrder = [1,2,4,8,9,5,10,3,6,7]
    InOrder = [8,4,9,2,10,5,1,6,3,7]
    t1 = createByPreInOder(preOrder,InOrder)

    preOrder = [1,2,4,8,5,3,6,7]
    InOrder = [8,4,2,5,1,6,3,7]
    t2 = createByPreInOder(preOrder,InOrder)
    
    preOrder2 = [2,4,8,5]
    InOrder2 = [8,4,2,5]
    t3 = createByPreInOder(preOrder2,InOrder2)
    
    print(isSubTree(t1,t3))
    print(isSubTree(t2,t3))
    
    print(isSubTree2(t1,t3))
    print(isSubTree2(t2,t3))
    
    
    



