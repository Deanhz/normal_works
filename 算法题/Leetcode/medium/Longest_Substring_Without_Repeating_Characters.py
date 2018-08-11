# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 22:09:27 2018

@author: Dean
3 medium
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
总结：这道题看似简单，虽然自己做出来了，但花了挺长时间，差不多40分钟，还是得参考一下别人的做法。
"""

class Solution:
    def lengthOfLongestSubstring(self, s):# by me
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        max_length = 0
        n = len(s)
        j = 1
        for i in range(n): 
            while(j<n+1):
                cur = s[i:j]
                length = len(cur)
                max_length = length if length > max_length else max_length
                if j >= n :
                    break
                if s[j] not in cur:
                    j = j + 1
                else:
                    break
        
        return max_length
    
    def lengthOfLongestSubstring2(self, s): # ths best
        if not s:
            return 0
        start = max_len = 0
        dic = {}
        for i,c in enumerate(s):
            if c in dic and dic[c] >= start: #这个条件很重要，尤其是后半部分。
                start = dic[c] + 1
            else:
                max_len = max(max_len,i-start+1)
            dic[c] = i
        return max_len
        
        
    
if __name__ == "__main__":
    s = "tmmzuxt"
    print(Solution().lengthOfLongestSubstring2(s))
                
        

