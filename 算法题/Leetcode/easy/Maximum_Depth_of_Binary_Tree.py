'''
2017.11.1
104 easy
Given a binary tree, find its maximum depth.
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):  # by me,recursion
        '''
        :type root: TreeNode
        :rtype: int
        '''
        if not root:
            return 0
        ldepth = self.maxDepth(root.left)
        rdepth = self.maxDepth(root.right)
        if ldepth > rdepth:
            return ldepth + 1
        else:
            return rdepth + 1

    def maxDepth2(self, root):  # by me,non-recursion
        if not root:
            return 0
        Q = [root]
        level = 0
        last = root
        while(Q):
            curr = Q.pop(0)
            if curr.left:
                Q.append(curr.left)
            if curr.right:
                Q.append(curr.right)
            if curr == last:
                level += 1
                if Q:
                    last = Q[-1]
        return level

    def maxDepth3(self, root):  # by others, recursion
        return self.helper(root, 0)

    def helper(self, root, level):
        if not root:
            return level
        return max(self.helper(root.left, level + 1), self.helper(root.right, level + 1))


if __name__ == '__main__':
    pass
