'''
2017.9.23
58.
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.
'''


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        sentence = s.strip().split(' ')
        return len(sentence[-1])


if __name__ == '__main__':
    test = "a "
    print(Solution().lengthOfLastWord(test))
