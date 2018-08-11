# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 15:51:42 2018

@author: Dean
59 medium
参考上一题
"""

class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n < 1:
            return []
        if n == 1:
            return [[1]]
        left = 0
        right = n-1
        top = 0
        bottom = n-1
        result = [[0 for j in range(n)] for i in range(n)]
        k = 1
        while(k<=n*n):
            for j in range(left,right+1):
                result[top][j] = k
                k += 1
            if k >= n*n:
                break
            for i in range(top+1, bottom):
                result[i][right] = k
                k += 1
            for j in range(left,right+1)[::-1]:
                result[bottom][j] = k
                k += 1
            for i in range(top+1,bottom)[::-1]:
                result[i][left] = k
                k += 1
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return result


if __name__ == "__main__":
    print(Solution().generateMatrix(3))
    print(Solution().generateMatrix(4))
    print(Solution().generateMatrix(5))
                