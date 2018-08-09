# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 10:10:20 2018

@author: Dean
p191
"""

'''
问题1：
给定数组arr,arr中的所有值都为正数且不重复。每个值代表一种面值的货币，每种面值的货币可以
使用任意张，再给定一个整数aim代表要找的钱数，求组成aim的最少货币数。
举例：
arr=[5,2,3], aim=20
返回4
arr = [5,2,3], aim=0
返回0
arr=[3,5], aim=2
找不开,返回-1
'''
MAX = float("inf")

def minNum1(arr,aim):#时间度复杂度O(M*N),空间复杂度O(M*N)
    if not arr or aim < 0:
        return -1
    n = len(arr)
    dp = [[0 for i in range(aim+1)] for j in range(n)]
    dp[0][0] = 0
    for j in range(1,aim+1):#更新第一行
        dp[0][j] = MAX
        if j >= arr[0] and dp[0][j - arr[0]] != MAX:#判断货币0是否能用，是否找的开
            dp[0][j] = dp[0][j - arr[0]] + 1
    #更新第一列全是0，由于默认都是0，所以省去这部分代码。
    
    for i in range(1,n):
        for j in range(1,aim+1):
            if j >= arr[i] and dp[i][j-arr[i]] != MAX:#判断货币i是否能用，是否找的开
                dp[i][j] = min(dp[i][j-arr[i]]+1,dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n-1][aim] if dp[n-1][aim] !=MAX else -1

def minNum2(arr,aim):#空间压缩后，空间复杂度O(aim)
    if not arr or aim < 0:
        return -1
    n = len(arr)
    dp = [0 for j in range(aim+1)]
    dp[0] = 0
    for j in range(1,aim+1):
        dp[j] = MAX
        if j >= arr[0] and dp[j - arr[0]] != MAX:
            dp[j] = dp[j-arr[0]] + 1
    for i in range(1,n):
        for j in range(1,aim+1):
            if j >= arr[i] and dp[j-arr[i]] != MAX:
                dp[j] = min(dp[j],dp[j-arr[i]]+1)
            else:
                dp[j] = dp[j]
    return dp[j] if dp[j] != MAX else -1

def minNum_by_me1(arr,aim): #by me , dp[i][j]重新定义
    if not arr or aim < 0:
        return -1
    n = len(arr)
    #dp[i][j]表示只使用arr[0..i-1]构成j最少的货币数
    dp = [[0 for j in range(aim+1)] for i in range(n+1)]
    #dp[0][j] = MAX 不适用任何货币无法构成，货币数设置为MAX
    for j in range(aim+1):
        dp[0][j] = MAX
    #dp[i][0] = 0 使用arr[0..i-1]构成0，货币数为0
    for i in range(n+1):
        dp[i][0] = 0
    for i in range(1,n+1):
        for j in range(1,aim+1):
            if j>= arr[i-1] and dp[i][j-arr[i-1]]!=MAX:
                dp[i][j] = min(dp[i][j-arr[i-1]]+1, dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][aim] if dp[n][aim] != MAX else -1
    
        
    

'''
问题2：
给定数组arr,arr中的所有值都为正数。每个值代表一张面值的货币，
再给定一个整数aim代表要找的钱数，求组成aim的最少货币数。
举例：
arr=[5,2,3], aim=20
找不开,返回-1
arr = [5,2,5,3], aim=10
返回2
arr = [5,2,5,3], aim=15
返回15
arr = [5,2,5,3], aim=0
返回0
'''

def minNum3(arr, aim):
    if not arr or aim < 0:
        return -1
    n = len(arr)
    dp = [[0 for j in range(aim+1)] for i in range(n)]
    dp[0][0] = 0
    for j in range(1,aim+1):
        dp[0][j] = MAX
    if arr[0] < aim:
        dp[0][arr[0]] = 1
    
    for i in range(1,n):
        for j in range(1,aim+1):
            if j >= arr[i] and dp[i-1][j-arr[i]]!=MAX:#使用这张钱一定能找开
                dp[i][j] = min(dp[i-1][j],dp[i-1][j-arr[i]]+1)
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n-1][aim] if dp[n-1][aim] != MAX else -1

def minNum4(arr, aim):#空间压缩后，空间复杂度O(aim)
    if not arr or aim < 0:
        return -1
    n = len(arr)
    dp = [0 for i in range(aim+1)]
    dp[0] = 0
    for j in range(1,aim+1):
        dp[j] = MAX
    if arr[0] < aim:
        dp[arr[0]] = 1
    for i in range(1,n):
        for j in range(1,aim+1)[::-1]:
            if j >= arr[i] and dp[j-arr[i]] != MAX:
                dp[j] = min(dp[j],dp[j-arr[i]]+1)
            else:
                dp[j] = dp[j]
    return dp[aim] if dp[aim] !=MAX else -1

def minNum_by_me2(arr,aim): #by me , dp[i][j]重新定义
    if not arr or aim < 0:
        return -1
    n = len(arr)
    #dp[i][j]表示只使用arr[0..i-1]构成j最少的货币数
    dp = [[0 for j in range(aim+1)] for i in range(n+1)]
    #dp[0][j] = MAX 不适用任何货币无法构成，货币数设置为MAX
    for j in range(aim+1):
        dp[0][j] = MAX
    #dp[i][0] = 0 使用arr[0..i-1]构成0，货币数为0
    for i in range(n+1):
        dp[i][0] = 0
    for i in range(1,n+1):
        for j in range(1,aim+1):
            if j>= arr[i-1] and dp[i-1][j-arr[i-1]]!=MAX:
                dp[i][j] = min(dp[i-1][j-arr[i-1]]+1, dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][aim] if dp[n][aim] != MAX else -1

if __name__ == "__main__":
    arr = [5,2,3]
    aim = 20
    arr2 = [5,2,5,3]
    aim2=10
    print(minNum1(arr,aim))
    print(minNum2(arr,aim))
    print(minNum_by_me1(arr,aim))
    print(minNum3(arr2,aim2))
    print(minNum4(arr2,aim2))
    print(minNum_by_me2(arr2,aim2))



