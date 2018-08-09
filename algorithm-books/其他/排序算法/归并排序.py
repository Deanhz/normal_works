# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 20:57:34 2018

@author: Dean
"""

def merge(arr, low, mid, high): #arr[low..mid]和arr[mid+1..high]各自有序，合并成一个有序表
    buf = arr.copy()
    i = low
    j = mid + 1
    k = low
    while(i <= mid and j <= high):
        if buf[i] <= buf[j]:
            arr[k] = buf[i]
            i += 1
        else:
            arr[k] = buf[j]
            j += 1
        k += 1
    while(i <= mid):
        arr[k] = buf[i]
        i += 1
        k += 1
    while(j <= high):
        arr[k] = buf[j]
        j += 1
        k += 1
    del(buf)

def MergeSort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        MergeSort(arr,low, mid)
        MergeSort(arr,mid+1, high)
        merge(arr, low, mid ,high)

if __name__ == "__main__":
    test = [53,17,78,9,45,65,87,32]
    test2 = [51,2,65,3,6,5,86,15,12,7,24]
    MergeSort(test,0,len(test)-1)
    MergeSort(test2,0,len(test2)-1)
    print(test)
    print(test2)
    
