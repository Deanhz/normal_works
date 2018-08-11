'''
2017.11.1
100 easy
Given two binary trees, write a function to check if they are equal or not.
Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree(self, p, q):  # by me
        '''
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        '''
        if(not p and not q):
            return True
        elif(not p or not q):
            return False
        elif(p.val == q.val):
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
