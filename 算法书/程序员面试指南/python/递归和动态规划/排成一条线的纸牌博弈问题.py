# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 20:18:52 2018

@author: Dean
p233
"""

def func(arr):# by me，时间复杂度O(N),空间复杂度O(1)
    if not arr:
        return 0
    N = len(arr)
    i = 0
    j = N - 1
    sumA = 0
    sumB = 0
    isA = True
    while(i <= j): 
#        print(i,j)
        left = max(arr[i+1],arr[j]) - arr[i]
        right = max(arr[i],arr[j-1]) - arr[j]
        val = 0        
        if left < right:
            val = arr[i]
            i += 1
        else:
            val = arr[j]
            j -= 1
        if isA:
            sumA += val
#            print("sumA:",sumA)
            isA = False
        else:
            sumB += val
#            print("sumB:",sumB)
            isA = True
    return max(sumA,sumB)

if __name__ == '__main__':
    arr = [1, 2, 100, 4]
    print(func(arr))
    arr2 = [1, 100, 2]
    print(func(arr2))
        





