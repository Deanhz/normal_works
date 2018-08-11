# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 18:50:54 2018

@author: Dean
118 easy Array
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.
Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
总结：不难，思考一下即可
"""

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        if numRows == 1:
            return [[1,],]
        result = [[1,],[1,1],]
        if numRows == 2:
            return result
        for i in range(2,numRows):
            tmp = []
            tmp.append(1)
            for j in range(i-1):
                tmp.append(result[i-1][j] + result[i-1][j+1])
            tmp.append(1)
            result.append(tmp)
        return result
    
if __name__ == "__main__":
    print(Solution().generate(5))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

