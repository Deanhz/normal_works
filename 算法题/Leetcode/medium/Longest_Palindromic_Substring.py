# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 21:35:14 2018

@author: Dean
5 medium 
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
总结：看似简单，实际很有难度，重点学习！
解决方法参考：
https://leetcode.com/problems/longest-palindromic-substring/solution/
采用上面的方法1，求出s的逆，然后转化为最长公共子串为题。
注意，公共子串不一定是正确结果。
比如，S=”abacdfgdcaba”，S​′=”abacdgfdcaba”。
公共子串”abacd”并不是回文。
方法2：动态规划。
leetcode上提交超时了，第一个方法测试样例通过90/94，第二个方法87/94
"""
class Solution:
    def longestPalindrome(self, s):#时间复杂度o(n^2),空间复杂度o(n^2)
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        s_ = s[::-1]
        lcs = self.LCS(s,s_)
        return lcs
    
    def LCS(self,s1, s2):#时间复杂度O(n**2)
        if not s1 or not s2:
            return ""
        len1 = len(s1)
        len2 = len(s2)
        start1 = -1 
        start2 = -1 
        c = [[0 for i in range(len2+1)] for j in range(len1+1)]
        max_length = 0
        max_substr = ""
        for i in range(len1+1):
            for j in range(len2+1):
                if i == 0 or j == 0:
                    c[i][j] = 0
                elif s1[i-1] == s2[j-1]:
                    c[i][j] = c[i-1][j-1] +1
                    
                    sublen = c[i][j]
                    sub1 = i - c[i][j]
                    sub2 = j - c[i][j]
                    subStr = s1[sub1:i]
                    reverse_start = len1 - (sub1 + sublen) #判断sub2的子串是不是s1的子串逆转而来的。
                    if sublen > max_length and reverse_start == sub2:
                        max_substr = subStr
                        max_length = sublen
                        start1 = i - c[i][j]
                        start2 = j - c[i][j]
                else:
                    c[i][j] = 0
        return max_substr
    
    def longestPalindrome2(self, s):#时间复杂度o(n^2),空间复杂度o(n^2)
        length = len(s)
        #p[i][j]=True,说明si,...,sj是回文
        #p[i][i] = True,p[i][i+1] = (si==sj)
        #p[i,j] = (p[i+1][j-1] and si==sj)
        p = [[False for i in range(length)] for j in range(length) ]
        max_subLen = 0
        max_subStr = ""
#        for i in range(length):
#            p[i][i] = True
        for i in range(length)[::-1]:#i从大到小
            for j in range(i,length):#j从小到大
                subStr = s[i:j+1]
                subLen = j - i + 1
#                print(i,j)
                if subLen == 1:
                    p[i][j] = True
                elif subLen == 2:
                    p[i][j] = (s[i] == s[j])
                else:
                    p[i][j] = p[i+1][j-1] if s[i]==s[j] else False
#                print(subStr,p[i][j],subLen)
                if p[i][j] and (subLen > max_subLen):
                    max_subStr = subStr
                    max_subLen = subLen
        
        return max_subStr
        
        
if __name__ == "__main__":
    test = "aaaa"
    print(Solution().longestPalindrome2(test))

