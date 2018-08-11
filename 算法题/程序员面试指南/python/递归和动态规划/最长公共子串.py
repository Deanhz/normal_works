# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 21:37:57 2018

@author: Dean
空间复杂度为O(1)的方法巧妙。
"""

def getdp(str1, str2):
    if not str1 or not str2:
        return ""
    len1 = len(str1)
    len2 = len(str2)
    dp = [[0 for j in range(len2)] for i in range(len1)]
    for i in range(len1):
        if str1[i] == str2[0]:
            dp[i][0] = 1
    for j in range(len2):
        if str1[0] == str2[j]:
            dp[0][j] = 1
    for i in range(1, len1):
        for j in range(1, len2):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = 0
    return dp

def lcss1(str1,str2):#时间复杂度O(M*N),空间复杂度O(M*N)
    if not str1 or not str2:
        return ""
    dp = getdp(str1,str2)
    end = 0
    max_ = 0
    for i in range(len(str1)):
        for j in range(len(str2)):
            if dp[i][j] > max_:
                max_ = dp[i][j]
                end = i
    return str1[end+1-max_:end+1]

def lcss2(str1, str2):#空间复杂度O(1),巧妙
    if not str1 or not str2:
        return ""
    len1 = len(str1)
    len2 = len(str2)
    row = 0 #斜线开始的行
    col = len2 - 1 #斜线开始的列
    max_ = 0 #记录最大的长度
    end = 0 #最大长度更新时，记录子串的结束位置
    while(row < len1):
        i = row
        j = col
        len_tmp = 0
        while(i < len1 and j < len2):#从(i,j)开始向右下方遍历
            if str1[i] == str2[j]:
                len_tmp += 1
            else:
                len_tmp = 0
            if len_tmp > max_ :
                max_ = len_tmp
                end = i
            i += 1
            j += 1
        if col > 0:
            col -= 1
        else:
            row += 1
    return str1[end + 1 - max_:end + 1]

            

if __name__ == "__main__":
    str1 = "1AB2345CD"
    str2 = "12345EF"
    result = lcss1(str1,str2)
    result2 = lcss2(str1,str2)
    print(result)
    print(result2)
    
    
    