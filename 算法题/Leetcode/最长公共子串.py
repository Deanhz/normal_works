# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 09:47:54 2018

@author: Dean
(LCS：Longest Common Substring)

"""

def LCS(s1, s2):#时间复杂度O(n**2)
    if not s1 or not s2:
        return ""
    len1 = len(s1)
    len2 = len(s2)
    start1 = -1 # 最长公共子串在s1的起点
    start2 = -1 # 最长公共子串在S2的起点
    #c[i][j]保存，s1第i个字符结尾的子串和s2第j个结尾的子串的最长公共子串的长度
    c = [[0 for i in range(len2+1)] for j in range(len1+1)]
    max_length = 0
    max_substr = ""
    for i in range(len1+1):
        for j in range(len2+1):
            if i == 0 or j == 0:
                c[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                c[i][j] = c[i-1][j-1] +1
                if c[i][j] > max_length:
                    max_length = c[i][j]
                    start1 = i - c[i][j]
                    start2 = j - c[i][j]
                    max_substr = s1[start1:i]
            else:
                c[i][j] = 0
    return max_length,max_substr,start1,start2

if __name__ == "__main__":
    s1 = "ABAB"
    s2 = "BABA"
    print(LCS(s1,s2))