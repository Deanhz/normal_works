# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 18:49:10 2018

@author: Dean

给定数组arr,arr中所有的值都为正数且不重复。每个值代表一种面值的货币，
每种面值的货币可以使用任意张，再给定一个正数aim代表要找的钱数，求换钱有
多少种方法。
举例：
arr=[5,10,25,1], aim=0
都不用,返回1。
arr = [5,10,25,1], aim=15
返回6
arr = [3,5], aim= 2
无法组成,返回0
"""

#暴力递归方法
def coins1(arr,aim):
    if not arr or aim < 0:
        return 0
    return process1(arr,0,aim)

def process1(arr,index,aim):#求使用arr[index..N-1]这些面值的钱组成aim的方法总数
    result = 0
    if index == len(arr):
        if aim == 0:
            return 1
        else:
            return 0

    else:
        i = 0
        while(arr[index] * i <= aim):
            result += process1(arr,index + 1, aim - arr[index] * i)
            i += 1
    return result
#记忆搜索优化
def coins2(arr,aim):
    if not arr or aim < 0:
        return 0
    n = len(arr)
    map_ = [[-1 for i in range(aim+1)] for j in range(n+1)]
    return process2(arr,0,aim,map_)

def process2(arr, index, aim, map_):
    result = 0
    if index == len(arr):
        if aim == 0:
            return 1
        else:
            return 0
    else:
        i = 0
        while(arr[index] * i <= aim):
            mapValue = map_[index+1][aim-arr[index]*i]
            if mapValue != -1:
                result += mapValue
            else:
                result += process2(arr,index+1,aim-arr[index]*i,map_)
            i += 1
    map_[index][aim] = result
    return result

#动态规划
def coins3(arr, aim):#时间复杂度O(n*aim^2)
    if not arr or aim<0:
        return 0
    n = len(arr)
    #dp[i][j]表示在使用arr[0..i]货币的情况下，组成钱数j有多少种方法。
    dp = [[0 for j in range(aim+1)] for i in range(n)]
    for i in range(n):
        dp[i][0] = 1
    for j in range(aim+1):
        if j % arr[0] == 0:
            dp[0][j] = 1
    for i in range(1,n):
        for j in range(1,aim+1):
            num = 0
            k = 0
            while(arr[i]*k <= j):
                num += dp[i-1][j-arr[i]*k]
                k += 1
            dp[i][j] = num
    return dp[n-1][aim]
#动态规划优化后
def coins4(arr, aim):#时间复杂度O(n*aim)
    if not arr or aim<0:
        return 0
    n = len(arr)
    #dp[i][j]表示在使用arr[0..i]货币的情况下，组成钱数j有多少种方法。
    dp = [[0 for j in range(aim+1)] for i in range(n)]
    for i in range(n):
        dp[i][0] = 1
    for j in range(aim+1):
        if j % arr[0] == 0:
            dp[0][j] = 1
    for i in range(1,n):
        for j in range(1,aim+1):
            noUseI_res = dp[i-1][j]
            UseI_res = dp[i][j - arr[i]] if j >= arr[i] else 0 
            dp[i][j] = noUseI_res + UseI_res
    return dp[n-1][aim]

#动态规划，空间压缩后
def coins5(arr, aim):
    if not arr or aim <0:
        return 0
    n = len(arr)
    dp = [0 for i in range(aim+1)]
    for i in range(aim+1):
        if i % arr[0] == 0:
            dp[i] = 1
    for i in range(1,n):
        for j in range(1,aim+1):
            dp[j] = dp[j] + dp[j -arr[i]] if j >= arr[i] else dp[j]
    return dp[aim]
            
if __name__ == "__main__":
    arr1 = [5,10,25,1]
    aim1 = 0
    arr2 = [5,10,25,1]
    aim2 = 15
    arr3 = [3,5]
    aim3 = 2
    print(coins1(arr1,aim1))
    print(coins1(arr2,aim2))
    print(coins1(arr3,aim3))
    
    print(coins2(arr1,aim1))
    print(coins2(arr2,aim2))
    print(coins2(arr3,aim3))
    
    print(coins3(arr1,aim1))
    print(coins3(arr2,aim2))
    print(coins3(arr3,aim3))
    
    print(coins4(arr1,aim1))
    print(coins4(arr2,aim2))
    print(coins4(arr3,aim3))
    
    print(coins5(arr1,aim1))
    print(coins5(arr2,aim2))
    print(coins5(arr3,aim3))
    
    