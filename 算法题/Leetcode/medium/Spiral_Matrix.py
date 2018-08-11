# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 14:36:07 2018

@author: Dean
54 medium
按照左到右，顶到底，右到左，底到顶的顺序循环，把遍历的元素加入到结果。

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = n-1
        top = 0
        bottom = m-1
        result = []
        while(left <= right and top <= bottom):
            #遍历最上一行
            for j in range(left, right+1):
                result.append(matrix[top][j])
            #遍历最右一列
            for i in range(top+1,bottom):
                result.append(matrix[i][right])
            #遍历最下一行
            for j in range(left,right+1)[::-1]:
                if top == bottom:
                    break
                result.append(matrix[bottom][j])
            #遍历最左一列
            for i in range(top+1,bottom)[::-1]:
                if left == right:
                    break
                result.append(matrix[i][left])
            left  += 1
            right -= 1
            top += 1
            bottom -= 1
        return result

if __name__ == "__main__":
    m1 = [
            [ 1, 2, 3 ],
            [ 4, 5, 6 ],
            [ 7, 8, 9 ]
            ]
    m2 = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]
    m3 = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]
    print(Solution().spiralOrder(m1))
    print(Solution().spiralOrder(m2))
    print(Solution().spiralOrder(m3))
    
    
    