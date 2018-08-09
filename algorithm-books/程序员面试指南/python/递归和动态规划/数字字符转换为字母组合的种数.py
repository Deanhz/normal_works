# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 19:39:50 2018

@author: Dean
p226
"""

def num1(str1): #时间复杂度O(N),空间复杂度O(N)
    if not str1:
        return 0
    N = len(str1)
    #dp[i]表示str[0..i-1]转换完，在str[i..N-1]还没转换的情况下，最终有多少种
    dp = [0 for i in range(N+1)]
    #初值
    dp[N] = 1
    if str1[N-1] != "0":
        dp[N-1] = 1
    else:
        dp[N-1] = 0
    #从后向前
    for i in range(N-1)[::-1]:
        if str1[i] == "0":
            dp[i] = 0
        else:
            if int(str1[i]) + int(str1[i+1]) < 27:
                dp[i] = dp[i+1] + dp[i+2]
    return dp[0]

def num2(str1): #降低空间复杂度，O(1)
    if not str1:
        return 0
    N = len(str1)
    next_ = 1
    cur = 0 #工作变量
    if str1[N-1] != "0":
        cur = 1
    for i in range(N-1)[::-1]:
        tmp = next_
        next_ = cur
        if str1[i] == "0":
            cur = 0
        else:
            if int(str1[i]) + int(str1[i+1]) < 27:
                cur = cur + tmp
    return cur




if __name__ == "__main__":
    test = ["1111", "01", "10"]
    for t in test:
        print(num1(t))
        print(num2(t))
