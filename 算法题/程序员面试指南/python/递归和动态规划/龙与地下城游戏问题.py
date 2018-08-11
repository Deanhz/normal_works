# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 20:44:57 2018

@author: Dean
本题的更新需要从下到上，从右到左
p223
"""

def minHP1(m):#时间复杂度O(M*N),空间复杂度O(M*N)
    if not m:
        return 1
    row = len(m)
    col = len(m[0])
    #dp[i][j]表示如果骑士走上位置(i,j)前,从该位置能够走到右下角，最少具备的血量
    dp = [[0 for j in range(col)] for i in range(row)]
    #初始化dp[row-1][col-1]
    #重要
    if m[row-1][col-1] > 0:
        dp[row-1][col-1] = 1
    else:
        dp[row-1][col-1] = 1 - m[row-1][col-1]
    #从右向左更新最后一行
    for j in range(col - 1)[::-1]:
        #dp不能小于1，因为血量随时都不能小于1
        dp[row-1][j] = max(dp[row-1][j+1] - m[row-1][j], 1)
    #从下到上，更新剩余行
    for i in range(row-1)[::-1]:
        #更新每行的最右端
        dp[i][col-1] = max(dp[i+1][col-1] - m[i][col-1], 1)
        for j in range(col-1)[::-1]:
            #水平方向
            dp_row = max(dp[i][j+1] - m[i][j], 1)
            #垂直方向
            dp_col = max(dp[i+1][j] - m[i][j], 1)
            #取最小值
            dp[i][j] = min(dp_col,dp_row)
    return dp[0][0]

def minHP2(m):#使用空间压缩,空间复杂度O(M*N)
    if not m:
        return 1
    row = len(m)
    col = len(m[0])
    dp = [0 for j in range(col)]
    #初始化dp[col-1]
    if m[row-1][col-1] > 0:
        dp[col-1] = 1
    else:
        dp[col-1] = 1 - m[row-1][col-1]
    #更新最后一行
    for j in range(col-1)[::-1]:
        dp[j] = max(dp[j+1] - m[row-1][j], 1)
    #更新剩余所有行
    for i in range(row-1)[::-1]:
        #更新每行的最右端
        dp[col-1] = max(dp[col-1] - m[i][col-1], 1)
        for j in range(col-1)[::-1]:
            #水平方向
            dp_row = max(dp[j+1] - m[i][j], 1)
            #垂直方向
            dp_col = max(dp[j] - m[i][j], 1)
            #取最小值
            dp[j] = min(dp_row, dp_col)
    return dp[0]
    
    

if __name__ == "__main__":
    m = [[-2, -3, 3],[-5, -10, 1], [0, 30, -5]]
    print(minHP1(m))
    print(minHP2(m))
            
    
    