# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 23:14:32 2018

@author: Dean
36 meidum 重要，尤其是在检查每一个子矩阵部分
检查数独矩阵是否合法

"""

class Solution:
    def isValidSudoku(self, board):# 时间复杂度O(3*n),n=81
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if not board or not board[0]:
            return False
        def isValid(buf,c):
            if c == ".":
                return True
            number = int(c)
            if buf[number]:
                return False
            else:
                buf[number] = True
                return True
        buf = [False for i in range(10)]
        #检查每一行
        for i in range(9):
            buf = [False for i in range(10)]
            for j in range(9):
                c = board[i][j]
                if not isValid(buf,c):
                    return False
        #检查每一列
        for i in range(9):
            buf = [False for i in range(10)]
            for j in range(9):
                c = board[j][i]
                if not isValid(buf,c):
                    return False                
        #检查每一个子矩阵是否有重复
        for i in range(0,9,3):
            for j in range(0,9,3):
                buf = [False for i in range(10)]
                for k in range(9):    
                    c = board[i+k//3][j+k%3]
                    if not isValid(buf,c):
                        return False
        
        return True

if __name__ == '__main__':
    m1 = [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
            ]
    m2 = [
            ["8","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
            ]
    print(Solution().isValidSudoku(m1))
    print(Solution().isValidSudoku(m2))
                    
                    