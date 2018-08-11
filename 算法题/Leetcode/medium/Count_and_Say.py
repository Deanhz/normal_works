# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 22:47:04 2018

@author: Dean
38 easy
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""

class Solution:
    def countAndSay(self, n): # by me
        """
        :type n: int
        :rtype: str
        """
        if n < 1:
            return ""
        result = ["" for i in range(n+1)]
        result[1] = "1"
        for i in range(2,n+1):
            lastStr = result[i-1]
            thisStr = ""
            lastc = lastStr[0]
            length = 0
            for c in lastStr:
                if c == lastc:
                    length += 1
                else:
                    thisStr += str(length) + lastc
                    lastc = c
                    length = 1
            thisStr += str(length) + lastc #这个地方容易忘，注意一下，特殊地方
            result[i] = thisStr
        return result[n]
    
if __name__ == "__main__":
    print(Solution().countAndSay(5))