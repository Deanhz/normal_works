# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 11:06:21 2018

@author: Dean
素数筛选法
"""

def func(n):#筛选出所有小于n的素数
    prime = [] #保存素数
    mark = [False for i in range(n)] #若mark[i]==True,则标记i为非素数
    for i in range(2,n):
        if mark[i]:
            continue
        prime.append(i) #找到一个素数
        j = i * i #从 i*i开始，而不是从i*2开始，因为i*k(k<i)已经在遍历k时被标记过了。
        while(j<n):
            mark[j] = True
            j = j + i
    return prime

print(func(100))
