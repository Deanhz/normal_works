# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 15:04:15 2018

@author: Dean

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
Given array nums = [-1,0,1,2,-1,-4], and target = -1.
Given array nums = [-5, -2, -1, 0, 0, 0, 1, 3, 5], and target = 6.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
总结：
方法类似3Sum，但是注意条件j>i+1。
因为当j=i+1,此时j是第一次循环，
当j>i+1时，才开始判断nums[j] == nums[j-1],判断本次循环的值和上次是否相等。
如果相等，去重，过滤。
测试样例参考：
nums = [-4, -1, -1, 0, 1, 2], and target = -1.
nums = [-5, -2, -1, 0, 0, 0, 1, 3, 5], and target = 6.
"""

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        n = len(nums)
        if n < 4 :
            return []
        result = []
        nums.sort()
        for i in range(n-3):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n-2):
                if j > i+1 and nums[j] == nums[j-1]: #注意条件j>i+1
                    continue
                l = j + 1
                r = n - 1
                while(l < r):
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s == target:
                        result.append([nums[i],nums[j],nums[l],nums[r]])
                        while(l < r and nums[l] == nums[l+1]):
                            l += 1
                        while(l < r and nums[r] == nums[r-1]):
                            r -= 1
                        l += 1
                        r -= 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
        return result
    
    
if __name__ == "__main__":
    print(Solution().fourSum([-4, -1, -1, 0, 1, 2],-1))
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

