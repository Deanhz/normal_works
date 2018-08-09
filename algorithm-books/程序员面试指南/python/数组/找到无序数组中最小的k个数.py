# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 17:00:52 2018

@author: Dean
p336
先排序的方法，时间复杂度最优是O(NlogN)。
本方法给出时间复杂度为O(Nlogk)。
方法：
维护一个有k个数的大根堆，选择出目前最小的k个数。
"""

def BuildMaxHeap(arr, n):
    i = n//2
    while(i >= 1):
        AdjustDown(arr, i, n)
        i -= 1
    return arr


def AdjustDown(arr, k, n):
    tmp = arr[k]
    i = 2 * k
    while(i <= n):
        if i < n and arr[i] < arr[i+1]:
            i += 1
        if tmp > arr[i]:
            break
        arr[k] = arr[i]
        k = i
        i = 2 * i
    arr[k] = tmp

def heapInsert(arr, index, value):
    if arr[1] > value:
        tmp = arr[1]
        arr[1] = value
        arr[index] = tmp
    return 
def getMinKNumsByHeap(arr, k):
    if not arr or k <= 0:
        return []
    arr.insert(0, 0)
    n = len(arr)
    BuildMaxHeap(arr,k)
    for i in range(k+1,n):
        if arr[1] > arr[i]:
            heapInsert(arr, i, arr[i])
            AdjustDown(arr, 1, k)
    arr.pop(0)
    return arr[:k]


    

if __name__ == "__main__":
    data = [6,4,77,43,13,40,17,29,34,23]
    data2 = list(range(10))[::-1]
    print(getMinKNumsByHeap(data, 5))
    print(getMinKNumsByHeap(data2, 5))
            
    
    
    





        


