'''
2017.10.17
67. easy
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100"
'''


class Solution(object):
    def addBinary(self, a, b):  # by me
        '''
        :type a: str
        :type b: str
        :rtype: str
        '''
        la = len(a)
        lb = len(b)
        maxL = max(la, lb)
        t_a = a[::-1]
        t_b = b[::-1]
        if la < lb:
            t_a = t_a + '0' * maxL
        else:
            t_b = t_b + '0' * maxL
        number = 0
        result = ''
        for i in range(maxL):
            sums = int(t_a[i]) + int(t_b[i]) + number
            result += str(sums % 2)
            number = sums // 2
            if (number == 1) and (i == maxL - 1):
                result += '1'
        result = result[::-1]
        return result


if __name__ == '__main__':
    print(Solution().addBinary('11', '1'))
