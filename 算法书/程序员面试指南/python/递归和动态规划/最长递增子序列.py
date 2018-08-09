# -*- coding: utf-8 -*-
"""
Created on Thu May 31 18:25:32 2018

@author: Dean
2018.5.31
p202
"""

def getdp(arr):#时间复杂度O(N^2)
    if not arr:
        return arr
    L = len(arr)
    dp = [1 for i in range(L)]
    for i in range(L):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[j] + 1,dp[i])
    return dp

def generateLIS(arr,dp):#时间复杂度O(N)
    if not arr:
        return arr
    L = len(arr)
    max_dp = 0
    max_dp_index = 0
    LIS = []
    for i in range(L):
        if dp[i] > max_dp:
            max_dp = dp[i]
            max_dp_index = i
    
    LIS.append(arr[max_dp_index])
    for i in range(max_dp_index)[::-1]:
        if dp[i] == dp[max_dp_index] - 1 and arr[i] < arr[max_dp_index]:
            LIS.insert(0, arr[i])
            max_dp_index = i
    return LIS

#时间复杂度为O(nlogn)的方法
def getdp2(arr):
    if not arr:
        return arr
    L = len(arr)
    ends = [0 for j in range(L)] #有效区
    ends[0] = arr[0]
    dp = [1 for j in range(L)]
    right = 0
    for i in range(1,L):
        l = 0
        r = right 
        while(l<=r):
            mid = (l+r)//2
            if ends[mid] < arr[i]:
                l = mid + 1
            else:
                r = mid - 1
        right = max(l,right)
        dp[i] = l + 1
        ends[l] = arr[i]
    return dp

if __name__ == "__main__":
    arr = [2, 1, 5, 3, 6, 4, 8, 9, 7]
    dp = getdp(arr)
    dp2 = getdp2(arr)
    LIS = generateLIS(arr,dp)
    print(dp)
    print(dp2)
#    print(LIS)
