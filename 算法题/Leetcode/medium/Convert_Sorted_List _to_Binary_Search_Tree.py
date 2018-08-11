# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 09:22:09 2018

@author: Dean
109 medium
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

Example:
Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

总结：类似108,简单
"""

# Definition for singly-linked list.
 class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

# Definition for a binary tree node.
 class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        data = []
        p = head
        while(p):
            data.append(p.val)
            p = p.next
        return self.BST(data)
    
    def BST(self, nums):
        if not nums:
            return None
        length = len(nums)
        mid = length // 2
        node = TreeNode(nums[mid])
        node.left = self.BST(nums[:mid])
        node.right = self.BST(nums[mid+1:])
        return node
    
    
    
    
    
    
        
        
        
        
        
        