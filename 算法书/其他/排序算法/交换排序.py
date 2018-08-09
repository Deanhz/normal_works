# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 18:16:44 2018

@author: Dean
"""

def BubbleSort(arr): # 时间复杂度O(n^2)
    if not arr:
        return 
    n = len(arr)
    for i in range(n):
        flag = False
        for j in range(i+1,n)[::-1]:
            if arr[j] < arr[j-1]:
                tmp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = tmp
                flag = True
        if not flag:
            break
    return arr

def QuikSort(arr,low,high):#时间复杂度平均O(nlogn)
    if low < high:
        pivotPos = partition(arr,low,high)
        QuikSort(arr,low,pivotPos-1)
        QuikSort(arr,pivotPos+1,high)
    return arr

def partition(arr,low,high):
    pivot = arr[low]
    while(low < high):
        while(low < high and arr[high] >= pivot):
            high -= 1
        arr[low] = arr[high]
        while(low < high and arr[low] <= pivot):
            low += 1
        arr[high] = arr[low]
    arr[low] = pivot
    return low
        


if __name__ == "__main__":
    data1 = [21, 32, 43, 98, 20, 45, 23, 4, 68, 86]
    data2 = [21, 32, 43, 98, 20, 45, 23, 4, 68, 86]
#    print(data)
    print(BubbleSort(data1))
    print(QuikSort(data2,0,len(data2)-1))
    
    
    
    