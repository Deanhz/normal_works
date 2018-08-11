# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 09:40:50 2018

@author: Dean
110 easy
Given a binary tree, determine if it is height-balanced.
总结：经典，多回顾
"""
# Definition for a binary tree node.
 class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        record = {0:1,1:True}
        self.judge(root, record)
        return record[1]
    
    def judge(self, root, record):
        if not root:
            record[0] = 0
            record[1] = True
            return
        if not root.left and not root.right:
            record[0] = 1
            record[1] = True
        self.judge(root.left,record)
        if not record[1]:
            return
        leftH = record[0]
        self.judge(root.right,record)
        if not record[1]:
            return
        rightH = record[0]
        record[0] = max(leftH,rightH) + 1
        if abs(leftH - rightH) > 1:
            record[1] = False
            return
        record[1] = True
        return
        
        
        
        
        
        
        
        
        
        
        
        
