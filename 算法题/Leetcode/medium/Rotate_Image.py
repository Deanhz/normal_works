# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 23:23:25 2018
48 meidum 
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).


旋转每次移动调换4个位置，这个4个位置调换之间的对应关系需要自己去寻找，这还是有一定难度的，需要举例子来观察。

举一个4*4的例子，模拟一下 matrix[0,1]
(0,1) => (1,3)
(1,3) => (3,2)
(3,2) => (2,0)
(2,0) => (0,1)

(i,j) => (j,n-1-i)
(j,n-1-i) => (n-1-i,n-1-j)
(n-1-i,n-1-j) => (n-1-j,i)
(n-1-j,i) => (i,j)
"""

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return [[]]
        n = len(matrix)
        for i in range(n//2):
            for j in range(i,n-1-i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = tmp
        return

if __name__ == "__main__":
    matrix1 = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
            ]
    matrix2 = [
              [ 5, 1, 9,11],
              [ 2, 4, 8,10],
              [13, 3, 6, 7],
              [15,14,12,16]
              ]
    Solution().rotate(matrix1)    
    Solution().rotate(matrix2)
    print(matrix1)    
    print(matrix2)    
