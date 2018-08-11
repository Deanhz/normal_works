# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 16:19:34 2018

@author: Dean
55 medium

题目：
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
             
思路：
动态规划。局部解是i+nums[i](能跳到的位置)，全局解是最大的局部解(最远能跳的位置),每次遍历
先判断能不能到达这一步(glob >=i?)，如果不符合就一定不能跳到最后。如果遍历结束，glob大于最后位置。
则返回真。
"""

class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        n = len(nums)
        glob = 0 #保存最远能跳到位置
        loc = 0
        result = True
        for i in range(n):
            #如果跳不到i，就一定跳不到最后
            if glob < i:
                result = False
                break
            loc = i + nums[i]
            glob = max(loc,glob)
        if glob >= n-1:
            result = True
        return result

if __name__ == "__main__":
    t1 = [2,3,1,1,4]
    t2 = [3,2,1,0,4]
    print(Solution().canJump(t1))
    print(Solution().canJump(t2))
