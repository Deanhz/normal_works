# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 22:44:59 2018

@author: Dean
34 meidum 二分查找
简单
"""

class Solution:
    def searchRange(self, nums, target): # by me
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        N = len(nums)
        left = 0
        right = N - 1
        start = -1
        end = -1
        while(left <= right):
            mid = (left + right) // 2
            if nums[mid] == target:
                start = mid
                end = mid
                while(start-1 >=0 and nums[start-1] == target):
                    start = start - 1
                while(end+1 < N and nums[end+1] == target):
                    end = end + 1
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return [start, end]
    
if __name__ == "__main__":
    nums = [5,7,7,8,8,10]
    print(Solution().searchRange(nums, 6))