# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 23:07:13 2018

@author: Dean
39 meidum 非常重要
回溯法
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

"""

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        N = len(candidates)
        candidates.sort() # 先排序，为了后面的剪枝操作
        result = []
        tmp = []
        def backtrack(res, tmp, target, candidates, index):
            if target < 0:
                return 
            if target == 0:
#                print(tmp)
                res.append(tmp.copy())#这个地方非常容易出错，应该追加的是copy,因为tmp是经常变化的list。
#                print(res)
                return
            for i in range(index, N):
                if candidates[i] > target: #剪枝
                    break
                tmp.append(candidates[i])
                backtrack(res, tmp, target - candidates[i], candidates, i)
                tmp.pop()
                
        backtrack(result, tmp, target, candidates, 0)
        return result

if __name__ == "__main__":
    candidates1 = [2, 3, 6, 7]
    target = 7
    candidates2 = [2, 3, 5]
    target2 = 8
    print(Solution().combinationSum(candidates1, target))
    print(Solution().combinationSum(candidates2, target2))
