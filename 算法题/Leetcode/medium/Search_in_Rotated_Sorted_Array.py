# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 22:22:29 2018

@author: Dean
33 medium 二分查找  
想不到

参考链接：
https://www.cnblogs.com/grandyang/p/4325648.html
"""

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        N = len(nums)
        left = 0
        right = N - 1
        while(left <= right):
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[right]:#右半部分一定有序
                if nums[mid] < target and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
            else: #左半部分一定有序
                if nums[mid] > target and nums[left] <= target:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
    
if __name__ == "__main__":
    data = [4,5,6,7,0,1,2]
    print(Solution().search(data,0))
