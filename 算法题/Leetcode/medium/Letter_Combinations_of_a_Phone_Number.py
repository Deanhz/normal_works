# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 20:40:28 2018

@author: Dean
medium
17.
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        map_ = {"2":['a','b','c'], "3":['d','e','f'], '4':['g','h','i'], '5':['j','k','l'],
                '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
        inputString = [map_[key] for key in digits]
        ans = []
        
        def findcombinations(inputString, index, res, ans):
            if len(res) == len(inputString):
                ans.append(res)
                return 
            for letter in inputString[index]:
                findcombinations(inputString, index+1, res + letter, ans)
            return
        findcombinations(inputString, 0, "", ans)
        return ans
    
if __name__ == "__main__":
    test = "23"
    print(Solution().letterCombinations(test))
        
            