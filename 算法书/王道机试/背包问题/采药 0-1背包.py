# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 10:33:01 2018

@author: Dean
0-1背包问题
每个物品仅能放一次

输入：
输入的第一行有两个整数 T（1 <= T <= 1000）和 M（1 <= M <= 100），T 代
表总共能够用来采药的时间，M 代表山洞里的草药的数目。
接下来的 M 行每行包括两个在 1 到 100 之间（包括 1 和 100）的的整数，
分别表示采摘某株草药的时间和这株草药的价值。
输出：
可能有多组测试数据，对于每组数据，
输出只包括一行，这一行只包含一个整数，表示在规定的时间内，可以采到
的草药的最大总价值。
样例输入：
70 3
71 100
69 1
1 2
样例输出：
3 
"""

def maxValue(T,M,arr):
    #dp[i][j]在不超过j的情况下，表示只放入0..i物品的最大价值
    dp = [[0 for j in range(T+1)] for i in range(M)]
    #第一行
    for j in range(T+1):
        if j >= arr[0][0]:
            dp[0][j] = arr[0][1]
        else:
            dp[0][j] = 0
    #第一列
    for i in range(M):
        dp[i][0] = 0
    for i in range(1,M):
        for j in range(1,T+1):
            if j - arr[i][0] >= 0:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-arr[i][0]]+arr[i][1])
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[M-1][T]

def maxValue2(T,M,arr):#空间压缩
    dp = [0 for j in range(T+1)]
    #first row
    for j in range(T+1):
        dp[j] = arr[0][1] if j>= arr[0][0] else 0
    #the rest of row
    for i in range(M):
        for j in range(T+1)[::-1]: #这里需要从后向前，以为dp[i][j]依赖于dp[i-1][j]和dp[i-1][j-w]
            if j - arr[i][0] >= 0:
                dp[j] = max(dp[j],dp[j-arr[i][0]]+arr[i][1])
    return dp[T]

def main():
    T,M = input("请输入T和M:").split(" ")
    arr = []
    for i in range(int(M)):
        a,b = input().split()
        arr.append([int(a),int(b)])
    print(maxValue(int(T),int(M),arr))

if __name__ == "__main__":
#    T,M = 70,3
#    arr=[[71,100],[69,1],[1,2]]
#    print(maxValue(T,M,arr))
#    print(maxValue2(T,M,arr))
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
