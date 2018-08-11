'''
2017.10.20
70. easy
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

'''


class Solution(object):
    def climbStairs(self, n):
        '''
        :type n: int
        :rtype: int
        '''
        if n == 1:
            return 1
        elif n == 2:
            return 2
        F = [0] * (n + 1)
        F[1] = 1
        F[2] = 2
        for i in range(3, n + 1):
            F[i] = F[i - 1] + F[i - 2]
        return F[n]


if __name__ == '__main__':
    print(Solution().climbStairs(3))
