# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 09:58:13 2018

@author: Dean
40 meidum 重要
本题和39类似，主要在于去重，注意如何判断去重

Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""

class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        candidates.sort()
        N = len(candidates)
        result = []
        tmp = []
        
        def backtrack(result, tmp, candidates, index, target):
            if target < 0:
                return
            if target == 0:
                result.append(tmp.copy())
                return 
            for i in range(index,N):
                if i > index and candidates[i] == candidates[i-1]:# 避免重复
                    continue
                if candidates[i] > target:#剪枝
                    break
                tmp.append(candidates[i])
                backtrack(result, tmp, candidates, i+1, target-candidates[i])
                tmp.pop()
        backtrack(result, tmp, candidates, 0, target)
        return result
    
if __name__ == "__main__":
    candidates1 = [10,1,2,7,6,1,5]
    target1 = 8
    print(Solution().combinationSum2(candidates1,target1))
        
        