# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 14:39:20 2018

@author: Dean
"""

class Node:
    def __init__(self,value=None):
        self.value = value
        self.left = None
        self.right = None

def create(d):
    if not d:
        return None
    data = d.copy()
    bt = Node(data.pop(0))
    R = bt
    while(data):
        left = Node(data.pop(0))
        right = Node(data.pop(0))
        R.left = left
        R.right = right
        R = right
    return bt
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

def inInOrderUnRecur(tree):
    if not tree:
        return
    stack = []
    while(stack or tree):
        if tree:
            stack.append(tree)
            tree = tree.left
        else:
            node = stack.pop()
            print(node.value,end=" ")
            tree = node.right
    print()
    return

def posOrderUnRecur(tree):
    if not tree:
        return
    stack = []
    stack.append(tree)
    cur = None
    last = -1 #这个地方前往不能写None，因为下面的判断中条件可能存在None
    while(stack):
        cur = stack[-1]
#        print(cur.value)
        if (cur.left and last!=cur.left and last!=cur.right ):#如果last!=cur.left,last!=cur.right,则说明cur.left一定没处理过
            stack.append(cur.left)
        elif(cur.right and last!=cur.right):
            stack.append(cur.right)
        else:
            print(cur.value,end=" ")
            stack.pop()
            last = cur
    print()
    
if __name__ == "__main__":
    data = [1,2,3,4,5,6,7,8,9]
    preOrder = [5,4,11,7,2,8,13,6,3,1]
    InOrder = [7,11,2,4,5,13,8,3,6,1]
    tree2 = createByPreInOder(preOrder,InOrder)
    tree = create(data)
    preOrderRecur(tree2)
    print()
    inOrderRecur(tree2)
    print()
    posOrderRecur(tree2)
    print()
    print()
    preOrderUnRecur(tree2)
    inInOrderUnRecur(tree2)
    posOrderUnRecur(tree2)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    