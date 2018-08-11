# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 11:34:17 2018

@author: Dean

给定数组arr,和目标值Sum,在arr中找到所有a,b,使得a+b=Sum。
arr中的数可能存在重复值。
"""

def SumTwo(arr,target):#时间复杂度:O(NlogN)+O(N) = O(NlogN) 
    if not arr:
        return []
    n = len(arr)
    result = []
    arr = sorted(arr)
    i = 0
    j = n - 1
    while(i < j):
        if i >=1 and arr[i] == arr[i-1]:#重复值则跳过
            i += 1
            continue
        if j <= n - 2 and arr[j] == arr[j+1]:#重复值，跳过
            j -= 1
            continue
        tmp = arr[i] + arr[j]
        if tmp == target:
            result.append([arr[i],arr[j]])
            i += 1
            j -= 1
        elif tmp < target:
            i = i + 1
        else:
            j = j - 1
    return result

if __name__ == "__main__":
    arr = [1,1,2,3,4,5,6,6]
    print(SumTwo(arr,7))
