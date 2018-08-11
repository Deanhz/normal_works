# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 20:07:01 2018

@author: Dean
15 medium
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
总结：看似简单，其实有难度！
方法:先排序，把3Sum问题退化为2Sum问题。注意排序的时候使用sort,而不是sorted。
使用sorted提交代码就超时。
直接写在一个函数中的时间要比写两个函数时间快一点。
这种类型的题，要特别注意去重，去重的方法就是先排序，然后再根据判断条件，跳过重复值。
这个条件很重要，可以参考3Sum和4Sum问题中的判断条件。
"""

class Solution:
    def threeSum(self, nums): #时间复杂度:O(N*2)，时间超过17%用户
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        n = len(nums)
        result = []
        nums.sort()
        for i in range(n-2):
            if i >= 1 and nums[i] == nums[i-1]:#i>=1,开始判断本次循环值是否和上次相等，相等则跳过，去重。
                continue
            else:
                self.twoSum(nums[i+1:],-nums[i],result)
        return result
    
    def twoSum(self, arr,target,result):
        if not arr:
            return 
        n = len(arr)
        i = 0
        j = n - 1
        while(i < j):
            if i >= 1 and arr[i] == arr[i-1]:
                i += 1
                continue
            if j <= n-2 and arr[j] == arr[j+1]:
                j -= 1
                continue
            tmp = arr[i] + arr[j]
            if tmp == target:
                result.append([-target,arr[i], arr[j]])
                i += 1
                j -= 1
            elif tmp < target:
                i += 1
            else:
                j -= 1
        return
    
    #整合在一个函数中
    def threeSum2(self, nums): #时间复杂度:O(N*2),时间超过21%用户
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        n = len(nums)
        result = []
        nums.sort()
        for i in range(n-2):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = n - 1
            while(l < r):
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    result.append([nums[i],nums[l],nums[r]])
                    while(l < r and nums[l] == nums[l+1]):
                        l += 1
                    while(l < r and nums[r] == nums[r-1]):
                        r -= 1                
                    l += 1
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
            
        return result
    
if __name__ == "__main__":
    arr = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum2(arr))
    
                
                
                
                
                
                
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        