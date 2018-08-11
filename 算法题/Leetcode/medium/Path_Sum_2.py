# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 15:22:49 2018

@author: Dean
113 medium

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]

总结：非递归后续遍历，非常重要，注意last=-1,因为这个地方浪费了一下午时间。
"""
def preOrderRecur(tree):
    if not tree:
        return
    print(tree.val,end=" ")
    preOrderRecur(tree.left)
    preOrderRecur(tree.right)
    return

def inOrderRecur(tree):
    if not tree:
        return
    inOrderRecur(tree.left)
    print(tree.val,end=" ")
    inOrderRecur(tree.right)
    return

def posOrderUnRecur(tree):
    if not tree:
        return
    stack = []
    stack.append(tree)
    cur = None
    last = -1
    while(stack):
        cur = stack[-1]
        if (cur.left and last!=cur.left and last!=cur.right ):
            stack.append(cur.left)
        elif(cur.right and last!=cur.right):
            stack.append(cur.right)
        else:
            print(stack.pop().val,end=" ")
            last = cur
    print()
def serialByPre(tree):#先序实现序列化，空用#表示，每个值后面都加“!”来分割。
    if(not tree):
        return "#!"
    val = str(tree.val) + "!"
    leftVal = serialByPre(tree.left)
    rightVal = serialByPre(tree.right)
    return val+leftVal+rightVal

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
def createByPreInOder(preOrder,InOrder):
    if not preOrder or not InOrder:
        return None
    length = len(preOrder)
    tree = TreeNode(preOrder[0])
    mid = 0
    for i in range(length):
        if InOrder[i] == preOrder[0]:
            mid = i
            break
    lenL = mid
    tree.left = createByPreInOder(preOrder[1:lenL+1],InOrder[:mid])
    tree.right = createByPreInOder(preOrder[lenL+1:],InOrder[mid+1:])
    return tree

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        self.func(root,sum,result)
        return result
    
    def func(self,root,Sum,result):
        stack = []
        stack.append(root)
        last = -1
        cur = None
        while(stack):
            cur = stack[-1]
            if(cur.left and last!=cur.left and last!=cur.right):
                stack.append(cur.left)
            elif (cur.right and last!=cur.right):
                stack.append(cur.right)
            else:
                if not cur.left and not cur.right:
                    route = [int(node.val) for node in stack]
#                    print(route)
                    sumVal = sum(route)
                    if sumVal == Sum:
                        result.append(route)
                stack.pop()
                last = cur
def posOrderRecur(tree):
    if not tree:
        return
    posOrderRecur(tree.left)
    posOrderRecur(tree.right)
    print(tree.val,end=" ")
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
            print(node.val,end=" ")
            tree = node.right
    print()
    return
if __name__ == "__main__":
    preOrder = [5,4,11,7,2,8,13,6,3,1]
    InOrder = [7,11,2,4,5,13,8,3,6,1]
    tree = createByPreInOder(preOrder,InOrder) 
    print(Solution().pathSum(tree,22))
