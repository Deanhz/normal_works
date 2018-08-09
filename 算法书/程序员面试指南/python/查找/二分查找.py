# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 22:01:00 2018

@author: Dean
递增序列的二分查找
"""

#查找等于key的数
def Binary_Search(arr,k):
    l = 0
    r = len(arr)-1
    mid = 0
    while(l<=r):
        mid = (l+r) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            l = mid + 1
        else:
            r = mid - 1
    return mid

#查找最左边比x大的数
def Binary_Search_left_max(arr,x):
    l,r = 0, len(arr)-1
    mid = 0
    while(l<=r):
        mid = (l+r)//2
        if arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return max(l,r)

#查找最右边比x小的数
def Binary_Search_right_min(arr,x):
    l,r = 0, len(arr)-1
    mid = 0
    while(l<=r):
        mid = (l+r)//2
        if arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return min(l,r)
           
   
   
   
   

if __name__ == "__main__":
    data = list(range(10))
    print(Binary_Search(data,5))
    
    data2 = [1,3,7,8,9,13]
    print(Binary_Search_left_max(data2,6))
    
    data2 = [1,3,7,8,9,13]
    print(Binary_Search_right_min(data2,10))