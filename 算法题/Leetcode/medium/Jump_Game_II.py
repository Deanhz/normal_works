# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 16:51:38 2018

@author: Dean
提交超时
"""

class Solution:
    
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)       
        if n == 1:
            return 0
        #dp[i]保存跳到最后最少需要的步数
        dp = [65535 for i in range(n)]
        #初始化
        dp[n-1] = 0
        for i in range(n-1)[::-1]:
            if nums[i] == 0: # 表示不可达
                continue
#            if nums[i] >= n - i - 1:
#                dp[i] = 1
#                continue
            min_step = min(dp[i+1:i+1+nums[i]])
            dp[i] = 1 + min_step
        return dp[0]
    def jump2(self, nums):
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return 0
        step = 0
        cur = 0 #表示只跳step步最远能能够到达的位置
        next_ = 0 #表示跳step+1步最远能够到达的位置
        for i in range(n):
            if cur < i:
                step += 1
                cur = next_
            next_ = max(next_, i + nums[i])
        return step

                
        
        
        
        

if __name__== "__main__":
    arr = [2,3,1,1,4]
    print(Solution().jump(arr))
    print(Solution().jump2(arr))
