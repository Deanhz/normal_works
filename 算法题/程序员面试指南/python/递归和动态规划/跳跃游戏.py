# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 20:39:21 2018

@author: Dean
p235
"""

def func(arr): # by me,时间复杂度O(N),空间复杂度O(N)
    if not func:
        return 0
    N = len(arr)
    #dp[i]表示从位置i,跳到最后最少需要的次数
    dp = [0 for i in range(N)]
    #初始化
    dp[N-1] = 0
    for i in range(N-1)[::-1]:
        #dp[i]
        min_step = min(dp[i + 1 : i + 1 + arr[i]])
        dp[i] = 1 + min_step
    return dp[0]


if __name__== "__main__":
    arr = [3,2,3,1,1,4]
    arr2 = [3,2,1,0,4]
    print(func(arr))