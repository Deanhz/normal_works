# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 20:42:14 2018

@author: Dean
96 medium
总结：难，没做出来。
该序列正好是卡特兰数。

"""

class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        #dp[i]表示有i个节点时，BST存在的情况数
        dp = [0 for i in range(n+1)]
        
        dp[0] = 1 #空节点，只有一种情况
        dp[1] = 1 #一个节点，只有一种情况
        for i in range(2,n+1):
            for j in range(i):#j表示左子树可能存在的个数
                dp[i] += dp[j] * dp[i-j-1] #总共有i个节点的情况总数等于：左子树的情况数 * 右子树的情况数
        return dp[n]

if __name__ == "__main__":
    print(Solution().numTrees(3))


