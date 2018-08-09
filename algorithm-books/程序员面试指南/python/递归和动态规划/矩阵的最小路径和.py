# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 23:09:42 2018

@author: Dean
p187
给定一个矩阵m，从左上角开始每次只能向右或者向下走，最后到达右下角的位置，路径上所有的
数字累加起来就是路径和，返回所有路径中最小的路径和
"""

def minPathSum1(m):#时间复杂度O(M*N),空间复杂度O(M*N)
    if not m or not m[0]:
        return 0
    row = len(m)
    col = len(m[0])
    #dp[i][j]表示从左上角(0,0)位置走到(i,j)位置的最小路径和
    dp = [[0 for i in range(col)] for j in range(row)]
    dp[0][0] = m[0][0]#勿忘
    
    #更新第0行
    for i in range(1,col):
        dp[0][i] = dp[0][i-1] + m[0][i]
    #更新第0列
    for i in range(1,row):
        dp[i][0] = dp[i-1][0] + m[i][0]
    
    for i in range(1,row):
        for j in range(1,col):
            dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + m[i][j]
    
    #回溯返回路径
    route = []
    route.append(m[row-1][col-1])
    i = row - 1
    j = col - 1
    while(i > 0 or j > 0):
        if dp[i][j] - m[i][j] == dp[i-1][j]:
            i = i - 1
        else:
            j = j - 1
        route.append(m[i][j])
    route = route[::-1]
    return dp[row-1][col-1],route

def minPathSum2(m):#空间压缩后，空间复杂度O(min(M,N))
    if not m or not m[0]:
        return 0
    row = len(m)
    col = len(m[0])
    rowmore = True
    more = less = -1
    if row >= col:
        rowmore = True
        more = row
        less = col
    else:
        rowmore = False
        more = col
        less = row
    
    dp = [0 for i in range(less)]
    dp[0] = m[0][0]
    for i in range(less):
        dp[i] = dp[i-1] + m[0][i] if rowmore else dp[i-1] + m[i][0]
    for i in range(1,more):
        dp[0] = dp[0] + m[i][0] if rowmore else dp[i-1] + m[0][i]
        for j in range(1,less):
            dp[j] = min(dp[j-1],dp[j]) + m[i][j] if rowmore else min(dp[j-1],dp[j]) + m[j][i]
    return dp[less - 1]
            
if __name__ == "__main__":
    m = [[1,3,5,9],[8,1,3,4],[5,0,6,1],[8,8,4,0]]
    print(minPathSum1(m))
    print(minPathSum2(m))
    



