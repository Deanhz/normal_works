# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 12:34:33 2018

@author: Dean
完全背包问题：
每个物品可以放任意次数

有一个储蓄罐，告知其空时的重量和当前重量，并给定一些钱币
的价值和相应的重量，求储蓄罐中最少有多少现金。

输入：
测试样例数T。
给定存钱罐的初始重量E和最终重量F。
N，硬币数。
硬币的价值P和硬币的重量W

总结：
有地方写错，导致浪费一下午时间
"""

MAX = float("inf")

def minDP(E,F,N,arr):#by me
    F = F - E #背包内钱的重量。
    #dp[i][j]表示使用硬币0..i，重量刚好为j时，最少的现金
    dp = [[0 for j in range(F+1)] for i in range(N)]
    #第一行
    dp[0][0] = 0
    for j in range(1,F+1):
        if j % arr[0][1]==0:
            dp[0][j] = j // arr[0][1] * arr[0][0] #这个地方写错了，导致浪费一下午的时间！
        else:
            dp[0][j] = MAX
    #第一列
    for i in range(1,N):
        dp[i][0] = 0
    #rest of
    for i in range(1,N):
        for j in range(1,F+1):
            if j >= arr[i][1] and dp[i][j-arr[i][1]]!=MAX:
                dp[i][j] = min(dp[i-1][j], dp[i][j-arr[i][1]]+arr[i][0])
            else:
                dp[i][j] = dp[i-1][j]
    if dp[N-1][F] == MAX:
        return "impossible"
    return dp[N-1][F]

def minDP2(E,F,N,arr):# by me
    F = F - E
    dp = [0 for i in range(F+1)]
    dp[0] = 0
    for j in range(1,F+1):
        if j % arr[0][1] == 0:
            dp[j] = j // arr[0][1] * arr[0][0]
        else:
            dp[j] = MAX
    for i in range(1,N):
        for j in range(arr[i][1],F+1):
            if dp[j-arr[i][1]]!=MAX:
                dp[j]=min(dp[j],dp[j-arr[i][1]]+arr[i][0])
    if dp[F] == MAX:
        return "impossible"
    return dp[F]

def minDP3(E,F,N,arr): #王道答案
    F = F - E
    dp = [MAX for i in range(F+1)]
    dp[0] = 0
    for i in range(1,N+1):
        for j in range(arr[i-1][1],F+1):
            if dp[j-arr[i-1][1]]!=MAX:
                dp[j]=min(dp[j],dp[j-arr[i-1][1]]+arr[i-1][0])
    if dp[F] == MAX:
        return "impossible"
    return dp[F]
    

if __name__ == "__main__":
    print(minDP(10,110,2,[[1,1],[30,50]]))
    print(minDP(10,110,2,[[1,1],[50,30]]))
    print(minDP(1,6,2,[[10,3],[20,4]]))
    print(minDP2(10,110,2,[[1,1],[30,50]]))
    print(minDP2(10,110,2,[[1,1],[50,30]]))
    print(minDP2(1,6,2,[[10,3],[20,4]]))

    print(minDP3(10,110,2,[[1,1],[30,50]]))
    print(minDP3(10,110,2,[[1,1],[50,30]]))
    print(minDP3(1,6,2,[[10,3],[20,4]]))