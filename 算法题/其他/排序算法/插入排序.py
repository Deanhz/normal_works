# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 20:42:06 2018

@author: Dean
"""
# 直接插入排序,最好O(n),平均O(n^2)。
# 边查找，边移动
def InsertSort(arr):
    if not arr:
        return arr
    n = len(arr)
    for i in range(1,n):
        cur = arr[i]
        j = i-1
        while(j>=0 and cur < arr[j]):#找到cur应该在的位置
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = cur
    return arr

#折半插入排序,先查找位置，再移动。查找的效率更高了。
def BinaryInsertSort(arr):
    if not arr:
        return arr
    n = len(arr)
    for i in range(1,n):
        cur = arr[i]
        low = 0
        high = i-1
        while(low<=high):
            mid = (low+high)//2
            if cur < arr[mid]:
                high = mid - 1
            else:
                low = high + 1
        j = i-1
        while(j >= high+1):
            arr[j+1] = arr[j]
            j -= 1
        arr[high+1] = cur
    return arr

#希尔排序,进行多次直接插入排序，每次直接插入排序的步长不断变化。
#步长为1时，就是普通的直接插入排序了。
def ShellSort(arr):#时间复杂度约为O(n^1.3), 最坏为O(n^2)
    if not arr:
        return arr
    n = len(arr)
    dk = n // 2
    while(dk >= 1):
        for i in range(dk,n):
            cur = arr[i]
            j = i-dk
            while(j>=0 and cur < arr[j]):
                arr[j+dk] = arr[j]
                j -= dk
            arr[j+dk] = cur
        dk = dk // 2
    return arr


if __name__ == "__main__":
    data = [5,4,1,7,9,3,6]
    print(InsertSort(data))
    print(BinaryInsertSort(data))
    print(ShellSort(data))
