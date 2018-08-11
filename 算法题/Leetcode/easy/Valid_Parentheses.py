'''
2017.9.14
20
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''


class Solution(object):
    def isValid(self, s):  # by me
        '''
        :type s:str
        :rtype: bool
        '''
        dic = {")": "(", "]": "[", "}": "{"}
        buf = []
        for char in s:
            if char in dic.values():
                buf.append(char)
            elif char in dic:
                try:
                    if dic[char] != buf.pop():
                        return False
                except Exception:
                    return False
            else:
                return False
        return buf == []


if __name__ == "__main__":
    print(Solution().isValid("()"))
