'''
2017.11.1
101 easy
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isRevSame(self, p, q):  # by me
        if(not p and not q):
            return True
        elif(not p or not q):
            return False
        elif(p.val == q.val):
            return self.isRevSame(p.left, q.right) and self.isRevSame(p.right, q.left)
        else:
            return False

    def isSymmetric(self, root):  # by me
        '''
        :type root: TreeNode
        :rtype: bool
        '''
        if not root:
            return True
        leftTree = root.left
        rightTree = root.right
        if(not leftTree and not rightTree):
            return True
        elif(not leftTree or not rightTree):
            return False
        else:
            return self.isRevSame(leftTree, rightTree)

    def equal(self, p, q):
        if(not p or not q):
            if(not p and not q):
                return True
            return False
        return p.val == q.val

    def isSymmetric2(self, root):  # by others
        if not root:
            return True
        stack = [root]
        while(stack):
            l = 0
            r = len(stack) - 1
            while(l <= r):
                if(not self.equal(stack[l].left, stack[r].right) or not self.equal(stack[l].right, stack[r].left)):
                    return False
                l += 1
                r -= 1
            tmp = []
            for node in stack:
                if(node.left):
                    tmp.append(node.left)
                if(node.right):
                    tmp.append(node.right)
            stack = tmp
        return True
