# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 09:11:34 2018

@author: Dean
108. easy

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

总结:简单，递归构建即可
"""

# Definition for a binary tree node.
 class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        return self.BST(nums)
        
    def BST(self, nums):
        if not nums:
            return None
        length = len(nums)
        mid = length // 2
        node = TreeNode(nums[mid])
        node.left = self.BST(nums[:mid])
        node.right = self.BST(nums[mid+1:])
        return node
        
        
        
        
        
        
        
