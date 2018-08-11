# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 10:28:25 2018

@author: Dean
112 easy
Given a binary tree and a sum, determine if the tree has a root-to-leaf path 
such that adding up all the values along the path equals the given sum.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
总结：看似简单，结果很费周折。犯了一个很易错的点，局部的bool变量传入函数，
这样函数是无法修改外部的局部变量，最终导致无效失败。应该把bool变量放入字典，传字典。
"""

# Definition for a binary tree node.
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

#错误解法！！
#class Solution:
#    def hasPathSum(self, root, sum):
#        """
#        :type root: TreeNode
#        :type sum: int
#        :rtype: bool
#        """
#        if not root:
#            return False
#        flag = False
#        self.func(root,sum,0,flag)
#        return flag
#    
#    def func(self, root, Sum, curSum,flag):
#        if not root:
#            return None
#        curSum += root.val
#        if not root.left and not root.right:
#            if curSum == Sum:
#
#                flag = True
#                return
#        if root.left:
#            self.func(root.left, Sum, curSum, flag)
#        if flag:
#            return
#        if root.right:
#            self.func(root.right, Sum, curSum, flag)
#        if flag:
#            return
#        return


class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        record = {0:False}
        self.func(root,sum,0,record)
        return record[0]
    
    def func(self, root, Sum, curSum, record):
        if not root:
            return None
        curSum += root.val
        if not root.left and not root.right:
            if curSum == Sum:

                record[0] = True
                return
            
        self.func(root.left, Sum, curSum, record)
        if record[0]:
            return
        
        self.func(root.right, Sum, curSum, record)
        if record[0]:
            return
        return
    
if __name__ == "__main__":
    preOrder = [5,4,11,7,2,8,13,4,1]
    InOrder = [7,11,2,4,5,13,8,4,1]
    tree = createByPreInOder(preOrder,InOrder)
    print(Solution().hasPathSum(tree,22))
    
    