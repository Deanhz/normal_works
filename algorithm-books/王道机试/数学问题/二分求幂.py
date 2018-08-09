# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 19:54:18 2018

@author: Dean

求 A^B 的最后三位数表示的整数。
1<=A,B<=10000
样例：
2 3
8

12 6
984
解题思路：
A^B结果的后三位，只与A的后三位和B有关。所以只保存中间结果的后三位，也就是对每一次乘法的结果取三位就可以。
整体思路就是按照二分求幂的方法，快速求幂。
"""

def func(a,b):
    if b == 0:
        return 1
    if b == 1:
        return a
    tmp = a
    res = 1
    while(b>0):
        if b % 2 == 1:#当前的二进制位如果为1，则累积。
            res = res * tmp
            res = res % 1000
        tmp *= tmp
        tmp %= 1000
        b = b // 2
    return res % 1000

if __name__ == "__main__":
    print(func(2,3))
    print(func(12,6))
