# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 14:03:41 2018

@author: Dean
43 medium
参考高精度整数乘法
"""

class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        n1 = len(num1)
        n2 = len(num2)
        num1 = num1[::-1]
        num2 = num2[::-1]
        tmp = [0 for i in range(n1+n2)]
        for i in range(n1):
            for j in range(n2):
                tmp[i+j] += int(num1[i]) * int(num2[j])
        c = 0
        result = []
        for i in range(n1+n2):
            tmp[i] += c
            c = tmp[i] // 10
            result.insert(0,str(tmp[i]%10))
        while(result and result[0] == "0"):
            result.pop(0)
        return "".join(result)

if __name__ == "__main__":
    print(Solution().multiply("250","125"))