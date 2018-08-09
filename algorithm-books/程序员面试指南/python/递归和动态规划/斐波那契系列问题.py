# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 16:39:57 2018

@author: Dean
p181
"""
#求斐波那契的第N项

def fibonacci1(n):#时间复杂度O(2^N)
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibonacci1(n-1) + fibonacci1(n-2)

def fibonacci2(n):# O(N)
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return 1
    res = 1
    pre = 1
    for i in range(3,n+1):
        tmp = res
        res = res + pre
        pre = tmp
    return res

#母牛问题,求第N年的牛总数
def cattle1(n): # O(2^N)
    if n < 1:
        return 0
    if n == 1 or n == 2 or n==3:
        return n
    return cattle1(n-1) + cattle1(n-3)

def cattle2(n): # O(N)
    if n < 1:
        return 0
    if n == 1 or n == 2 or n == 3:
        return n
    res = 3
    pre = 2
    prepre = 1
    for i in range(4,n+1):
        tmp = res
        res = res + prepre
        prepre = pre
        pre = tmp
    return res

if __name__ == "__main__":
    N = 5
    print(fibonacci1(N))
    print(fibonacci2(N))
    print(cattle1(N))
    print(cattle2(N))
        
    
    
    
    
    
    
    
    