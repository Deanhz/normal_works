# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 11:16:56 2018

@author: Dean
求正整数N的质因数的个数。 1<n<10^9
如：
120 = 2*2*2*3*5,共有5个质因数
"""
import math

def func(n):
    #先筛选出所有小于sqrt(num)的素数
    num = int(math.sqrt(n)) + 1
    prime = []
    mark = [False for i in range(num)] #标记非素数
    for i in range(2,num):
        if mark[i]:
            continue
        prime.append(i)
        for j in range(i*i,num,i):
            mark[j] = True
    resPrime = [] #保存分解出的素因数
    resExp = dict() #保存分解出的素因数对应的幂指数
    for i in prime:
        if n % i == 0: #说明素数i是n的素因数
            resPrime.append(i)
            resExp[i] = 0 #初始化
            while(n % i == 0):
                resExp[i] += 1
                n = n // i
        if n == 1:#若已经分解为1，该数已经被分解完毕，提前退出
            break
    
    if n != 1:# 若测试完小于sqrt(n)的所有素数仍未被分解为1，说明有一个大于sqrt(n)的素因数，并且仅有一个。
        resPrime.append(n)
        resExp[num] = 1
    return sum(resExp.values())
    
if __name__ == "__main__":
    print(func(120))
