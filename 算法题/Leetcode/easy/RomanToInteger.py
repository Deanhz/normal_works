'''
13.
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''


class Solution(object):
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def romanToInt(self, s):  # by me
        '''
        :type: str
        :rtype: int
        '''
        L = len(s)
        if L == 1:
            return self.dic[s]
        number = self.dic[s[L - 1]]
        for index in list(range(1, L))[::-1]:
            charR = s[index]
            charL = s[index - 1]
            numberR = self.dic[charR]
            numberL = self.dic[charL]
            if numberL < numberR:
                number = number - numberL
            else:
                number = number + numberL
        return number

    def romanToInt2(self, s):
        number = 0
        lastC = 'I'
        for c in s[::-1]:
            if self.dic[c] >= self.dic[lastC]:
                number += self.dic[c]
            else:
                number -= self.dic[c]
            lastC = c
        return number


if __name__ == "__main__":
    print(Solution().romanToInt2("MCMLXXX"))
