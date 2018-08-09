# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 17:53:08 2018

@author: Dean
最小编辑代价
p218

总结，本题的关键就在于递推公式，如果递推公式写出来，就容易解决。
递推公式有两种，第一种minCost1,dp[i][j]表示str1[0...i-1]编辑成str2[0...j-1]的代价，
dp[i][0]表示的是str1[0...i-1]编辑成 " "代价的，这种方法初始化dp的第一行和第一列比较容易。
而第二种dp[i][j]表示str1[0..i]编辑成str2[0..j]的代价，dp[0][j]表示的是str1[0]编辑成str2[0..j]
的代价，这种方法初始化有点麻烦。所以我们在定义dp[i][j]的时候究竟是表示0..i 和 0..j，
还是0..i-1还是0..j-1，要充分考虑一下。

"""

def minCost1(str1, str2, ic, dc, rc):#时间复杂度O(M*N),空间复杂度O(M*N)
    if not str1 or not str2:
        return 0
    len1 = len(str1)
    len2 = len(str2)
    #dp[i][j] 表示str1[0..i-1]编辑成str2[0..j-1]的代价
    dp = [[0 for j in range(len2 + 1)] for i in range(len1 + 1)]
    for i in range(1,len1 + 1):
        dp[i][0] = i*dc
    for j in range(1, len2 + 1):
        dp[0][j] = j * ic
    for i in range(1,len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j-1] + rc
            dp[i][j] = min(dp[i][j],dp[i-1][j] + dc)
            dp[i][j] = min(dp[i][j],dp[i][j-1] + ic)
    return dp[len1][len2]

def minCost2(str1, str2, ic, dc, rc):# 空间压缩后，空间复杂度O(N)
    if not str1 or not str2:
        return 0
    len1 = len(str1)
    len2 = len(str2)
    dp = [0 for j in range(len2 + 1)]
    for j in range(1,len2 + 1):
        dp[j] = j * ic
    for i in range(1, len1 + 1):
        pre = dp[0]
        dp[0] = i * dc
        for j in range(1,len2 + 1):
            tmp = dp[j]
            if str1[i-1] == str2[j-1]:
                dp[j] = pre
            else:
                dp[j] = pre + rc
            dp[j] = min(dp[j], dp[j-1] + ic)
            dp[j] = min(dp[j], tmp + dc)
            pre = tmp
    return dp[len2]

def minCost3(str1 ,str2, ic, dc, rc): #by me
    if not str1 or not str2:
        return 0
    len1 = len(str1)
    len2 = len(str2)
    #dp[i][j]表示str1[0...i]编辑成str2[0...j]的最小编辑代价
    dp = [[0 for j in range(len2)] for i in range(len1)]
    for j in range(len2):
        if str1[0] in str2[:j+1]:
            dp[0][j] = ic * j
        else:
            dp[0][j] = ic * (j+1) + dc
            dp[0][j] = min(dp[0][j], ic*j + rc )
    for i in range(len1):
        if str2[0] in str1[:i+1]:
            dp[i][0] = ic * i
        else:
            dp[i][0] = ic * (i+1) + dc
            dp[i][0] = min(dp[i][0],ic*i + rc)
    for i in range(1,len1):
        for j in range(1,len2):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j-1] + rc
            dp[i][j] = min(dp[i][j], dp[i][j-1] + ic)
            dp[i][j] = min(dp[i][j], dp[i-1][j] + dc)
    return dp[len1-1][len2-1]
    
    
        
if __name__ == "__main__":
    str1 = "ab12cd3"
    str2 = "abcdf"

    print(minCost1(str1, str2, 5, 3, 2))
    print(minCost2(str1, str2, 5, 3, 2))
    print(minCost3(str1, str2, 5, 3, 2))
        
    

