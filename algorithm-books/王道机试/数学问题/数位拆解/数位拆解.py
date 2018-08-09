# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 09:11:25 2018

@author: Dean

题目：
实现特殊乘法：
123*45 = 1*4 + 1*5 + 2*4 + 2*5 + 3*4 + 3*5 
输入：
123 45
输出:
    54
"""

def func():#普通的数位拆解法
    a,b = map(int,input().split())
    num1 = []
    num2 = []
    res = 0
    while(a>0):
        num1.insert(0,a%10)
        a = a // 10
    while(b>0):
        num2.insert(0, b%10)
        b = b // 10
    for i in num1:
        for j in num2:
            res += i*j
    return res

def func2():#特殊的数位拆解法,把它每个数当做字符串处理，遍历每个字符即可得到每一位数。
    res = 0
    a,b = input().split()  
    for i in a:
        for j in b:
            res = int(i)*int(j)
    return res

if __name__ == "__main__":
    print(func())
    print(func2())
