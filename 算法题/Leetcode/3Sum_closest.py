# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 14:44:04 2018

@author: Dean

Given an array nums of n integers and an integer target, 
find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. 
You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        n = len(nums)
        nums.sort()
        closest_target = ""
        closest_diff = float("inf")
        for i in range(n-2):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            l = i + 1 
            r = n - 1
            while(l < r):
                s = nums[i] + nums[l] + nums[r]
                diff = abs(s - target)
                if diff < closest_diff:
                    closest_diff = diff
                    closest_target = s
                if s == target:
                    return target
                if s < target:
                    l += 1
                else:
                    r -= 1
        return closest_target


if __name__ == "__main__":
    print(Solution().threeSumClosest([1,1,1,0],-100))
                
                
                
            
                