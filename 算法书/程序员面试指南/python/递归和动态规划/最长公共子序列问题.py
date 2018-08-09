# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 20:58:10 2018

@author: Dean
"""

def getdp(str1,str2):
    if not str1 or not str2:
        return None
    len1 = len(str1)
    len2 = len(str2)
    #dp[i][j]表示str1[0..i]和str2[0..j]的最长公共子序列的长度
    dp = [[0  for j in range(len2)] for i in range(len1)]
    dp[0][0] = 1 if str1[0] == str2[0] else 0
    for j in range(1,len2):
        if dp[0][j-1] == 1 or str1[0] == str2[j]:
            dp[0][j] = 1
    for i in range(1,len1):
        if dp[i-1][0] == 1 or str1[i] == str2[0]:
            dp[i][0] = 1
    
    for i in range(1,len1):
        for j in range(1,len2):
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            if str1[i] == str2[j]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
    return dp

def lcs(str1,str2):
    if not str1 or not str2:
        return None
    len1 = len(str1)
    len2 = len(str2)
    dp = getdp(str1,str2)
    result = []
    N  = dp[len1-1][len2-1]
    m = len1 - 1
    n = len2 - 1
    while(N > 0):
        if n >0 and dp[m][n] == dp[m][n-1]:
            n -= 1
        elif m > 0 and dp[m][n] == dp[m-1][n]:
            m -= 1
        else:
            result.insert(0,str1[m])
            N -= 1
            m -= 1
            n -= 1
    
    return "".join(result)

if __name__ == "__main__":
    str1 = "1A2C3D4B56"
    str2 = "B1D23CA45B6A"
    print(lcs(str1,str2))
    
    
    
            
            
            
            




