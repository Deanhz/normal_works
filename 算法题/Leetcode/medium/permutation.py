# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 22:03:39 2018

@author: Dean
46 medium 
回溯法
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        n = len(nums)
        result = []
        cur = []
        visited = [False for i in range(n)]
        def backtrack(result,cur,visited,level):
            if level == n:
                result.append(cur.copy()) #注意
                return
            for i in range(n):
                if visited[i]:
                    continue
                visited[i] = True
                cur.append(nums[i])
                backtrack(result,cur,visited,level+1)
                cur.pop()
                visited[i] = False
            
        backtrack(result,cur,visited,0)
        return result

if __name__ == "__main__":
    nums = [1,1,3]
    print(Solution().permute(nums))
    
    