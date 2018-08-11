# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 22:30:57 2018

@author: Dean
22 medium 回溯法
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        
        def backtrack(result, cur, n_open, n_close, n_max):
            if len(cur) == n_max * 2:
                result.append(cur)
                return
            if n_open < n_max:
                backtrack(result, cur+"(", n_open+1, n_close, n_max)
            if n_close < n_open: #注意这里的条件，只有右括号的个数小于左括号的个数才能添加右括号
                backtrack(result, cur+")", n_open, n_close+1, n_max)
                    
        backtrack(result, "", 0, 0, n)
        return result
        
if __name__ == "__main__":
    print(Solution().generateParenthesis(3))