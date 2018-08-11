'''
7.
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

Note:
The input is assumed to be a 32-bit signed integer.
Your function should return 0 when the reversed integer overflows.
'''


class Solution(object):
    def reverse(self, x):  # by me
        '''
        :type x: int
        :rtype: int
        '''
        num_list = list(str(x))
        flag = False
        if num_list[0] == '-':
            flag = True
            del num_list[0]
        num_list.reverse()
        if flag:
            num_list.insert(0, '-')
        num = int(''.join(num_list))
        if abs(num) >= 2**31 - 1:
            return 0
        return num

    def reverse2(self, x):
        sign = -1 if x < 0 else 1
        x *= sign

        # eliminated leading zero in reversed integer
        while x:
            if x % 10 == 0:
                x /= 10
            else:
                break
        x = list(str(x))
        x.reverse()
        x = "".join(x)
        x = int(x)
        return sign * x


if __name__ == '__main__':
    print(Solution().reverse2(-123))
