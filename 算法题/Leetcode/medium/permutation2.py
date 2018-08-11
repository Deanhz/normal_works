# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 22:27:37 2018

@author: Dean
47 medium
回溯法，去重
先排序
注意判断条件去重，在递归函数中，在递归函数中要判断前面一个数和当前的数是否相等，
如果相等，前面的数必须已经使用了，即对应的visited中的值为1，当前的数字才能使用，
否则需要跳过，这样就不会产生重复排列了
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

"""

class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
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
                if i > 0 and nums[i] == nums[i-1] and visited[i-1] == False:#避免重复，这里的判断条件需要注意
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
    print(Solution().permuteUnique(nums))