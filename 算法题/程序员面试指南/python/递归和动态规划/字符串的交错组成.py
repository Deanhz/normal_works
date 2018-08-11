# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 14:49:17 2018

@author: Dean
p220
"""

def isCross1(str1, str2, aim):#时间复杂度O(M*N),空间复杂度O(M*N)
    if not aim:
        return True
    if not str1 or not str2:
        return False
    len1 = len(str1)
    len2 = len(str2)
    len3 = len(aim)
    if len1 + len2 != len3:
        return False
    #dp[i][j]表示aim[0..i+j-1]能否被str1[0..i-1]和str2[0..j-1]交错组成
    dp = [[False for j in range(len2+1)] for i in range(len1+1)]
    #首元素
    dp[0][0] = True
    #第一列
    #dp[i][0]表示aim[0..i-1]能否仅被str1[0..i-1]交错组成
    for i in range(1,len1 + 1):
        if str1[i-1] != aim[i-1]:
            break
        dp[i][0] = True
    #第一行，同理
    for j in range(1, len2+1):
        if str2[j-1] != aim[j-1]:
            break
        dp[0][j] = True
    for i in range(1,len1 + 1):
        for j in range(1,len2 + 1):
            #从左到右 或 从上到下
            if (dp[i-1][j] and str1[i-1] == aim[i+j-1]) or (dp[i][j-1] and str2[j-1] == aim[i+j-1]):
                dp[i][j] = True
    return dp[len1][len2]

def isCross2(str1, str2, aim):#空间压缩后,空间复杂度O(N)
    if not aim:
        return True
    if not str1 or not str2:
        return False
    len1 = len(str1)
    len2 = len(str2)
    len3 = len(aim)
    if len1 + len2 != len3:
        return False
    dp = [False for j in range(len2 + 1)]
    dp[0] = True
    #按行来更新
    #第一行
    for j in range(1, len2 + 1):
        if str2[j - 1] != aim[j - 1]:
            break
        dp[j] = True
    #更下剩余行
    for i in range(1,len1+1):
        if dp[0] and str1[i-1] == aim[i-1]:
            dp[0] = True
        else:
            dp[0] = False
        for j in range(1, len2 + 1):
            if (dp[j-1] and str2[j-1] == aim[i+j-1]) or (dp[j] and str1[i-1] == aim[i+j-1]):
                dp[j] = True
            else:
                dp[j] = False
    return dp[len2]
    
def isCross3(str1, str2, aim):# by me, 时间复杂度O(M + N),空间复杂度O(M + N)
    if not aim:
        return True
    if not str1 or not str2:
        return False
    len1 = len(str1)
    len2 = len(str2)
    len3 = len(aim)
    if len1 + len2 != len3:
        return False
    s1 = ""
    s2 = ""
    for c in aim:
        if c in str1:
            s1 += c
        else:
            s2 += c
    if s1 == str1 and s2 == str2:
        return True
    else:
        return False
    
    
if __name__ == "__main__":
    str1 = "AB"
    str2 = "12"
    aims = ["AB12", "A1B2", "A12B", "1A2B", "1AB2"]
    for aim in aims:
        print("isCross1: ",isCross1(str1,str2,aim))
        print("isCross2: ",isCross2(str1,str2,aim))
        print("isCross3: ",isCross3(str1,str2,aim))
        
    

