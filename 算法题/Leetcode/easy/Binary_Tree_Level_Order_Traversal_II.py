'''
2017.11.7
107 easy
Given a binary tree, return the bottom-up level order traversal of its nodes' values. 
(ie, from left to right, level by level from leaf to root).
给定一个二叉树，返回其节点值的自底向上的级别遍历 （即从左到右，从叶到根的层次）。
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):  # by me
        '''
        :type root: TreeNode
        :rtype: List[List[int]]
        '''
        if not root:
            return []
        Q = [root]
        level = 0
        last = root
        result = []
        tmp = []
        while Q:
            curr = Q.pop(0)
            tmp.append(curr.val)
            if curr.left:
                Q.append(curr.left)
            if curr.right:
                Q.append(curr.right)
            if curr == last:
                level += 1
                result.append(tmp)
                tmp = []
                if Q:
                    last = Q[-1]
        return result[::-1]
