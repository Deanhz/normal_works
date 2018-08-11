# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 15:57:50 2018

@author: Dean
"""

class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        visited = [False for i in range(n+1)]
        result = []
        def backtrack(result, visited, n, k, cur):
            if len(result) >= k:
                return
            if len(cur) == n:
                result.append(cur)
                return
            for j in range(1,n+1):
                if not visited[j]:
                    visited[j] = True
                    backtrack(result, visited, n, k, cur+str(j))
                    visited[j] = False
        backtrack(result, visited, n,k, "")
        return result[-1]

if __name__ == "__main__":
    print(Solution().getPermutation(4,9))