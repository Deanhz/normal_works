# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 10:14:30 2018

@author: Dean

最大公约数
欧几里得算法(辗转相除法)
"""

def gcd1(a,b):#递归
    if b == 0:#当b==0时,a即为所求
        return a
    else:
        return gcd1(b,a%b)

def gcd2(a,b):#非递归
    if a == 0 or b == 0:
        return max(a,b)
    while(b!=0):#当b==0时，a即为所求
        t = a % b
        a = b
        b = t
    return a

def lcm(a,b):
    return a*b//gcd1(a,b)

a = 49
b= 14
print(gcd1(a, b))
print(gcd2(a, b))
print(lcm(a, b))
