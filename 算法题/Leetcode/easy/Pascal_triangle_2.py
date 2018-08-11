# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 19:06:07 2018

@author: Dean
119 easy Array
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.

Example:

Input: 3
Output: [1,3,3,1]
总结：不难
"""



class Solution:
    def generate(self, rowIndex):
        if rowIndex <0:
            return []
        if rowIndex == 0:
            return [1,]
        if rowIndex == 1:
            return [1,1]
        lastRow = [1,1]
        for i in range(2,rowIndex + 1):
            curRow = []
            curRow.append(1)
            for j in range(i-1):
                curRow.append(lastRow[j] + lastRow[j+1])
            curRow.append(1)
            lastRow = curRow
        return curRow
    
if __name__ == "__main__":
    print(Solution().generate(3))
        
