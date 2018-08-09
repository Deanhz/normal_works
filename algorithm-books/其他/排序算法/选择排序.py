# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 19:48:57 2018

@author: user
注意！堆排序是把序列看成一颗完全二叉树的顺序存储结构。完全二叉树的编号从1~n！
不是从0开始，否则就找不到完全二叉树中双亲节点和孩子节点间的对应关系了！
堆排序写起来很麻烦，主要是用for循环有坑，所以都用while来写的。
"""

    


#简单选择排序
def SelectSort(arr):
    if not arr:
        return arr
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        tmp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = tmp
    return arr

#堆排序

#建立大根堆
def BuildMaxHeap(arr, n):
    i = n//2
    while(i>=1):
        AdjustDown(arr, i, n)
        i -= 1
    
    return arr

#调整以k为根的子树为大根堆、
def AdjustDown(arr, k, n):
    tmp = arr[k] #暂存的根节点
    #不断的向下调整
    i = 2*k
    while(i<n+1):
        if i < n and arr[i]<arr[i+1]: #去较大的子节点
            i += 1
        if tmp >= arr[i]:
            break
        else:
            arr[k] = arr[i]
            k = i # 当前来说,根节点正确的位置
            i = i * 2
    #把暂存的根节点放在正确的位置
    arr[k] = tmp

#大根堆，堆排序算法
def HeapSort(arr):
    n = len(arr)
    arr.insert(0,0) #在第一个位置插入一个值，我们只对arr[1..n]排序。
    arr = BuildMaxHeap(arr, n) #构建初始大根堆
    result = []
    i = n
    while(i>=2):
        #输出堆顶元素
        result.append(arr[1])
        #交换堆顶和堆底元素
        arr[1],arr[i] = arr[i],arr[1]
        AdjustDown(arr,1,i-1) #把剩余n-1的元素排成堆
        i -= 1
    result.append(arr[1])
    return result


#建立小根堆   
def BuildMinHeap(arr, n):
    i = n // 2
    while(i>=1):
        Adjustdown2(arr,i,n)
        i -= 1

#小根堆的向下调整
def Adjustdown2(arr, k, n):
    tmp = arr[k]
    i = k * 2
    while(i <= n):
        if i < n and arr[i+1] <  arr[i]:
            i += 1
        if tmp < arr[i]:
            break
        arr[k] = arr[i]
        k = i
        i = 2 * i
    arr[k] = tmp
#小根堆，堆排序
def HeapSort2(arr):
    if not arr:
        return arr
    n = len(arr)
    arr.insert(0,0)
    BuildMinHeap(arr, n)
    result = []
    i = n
    while(i>=2):
        result.append(arr[1])
        #swap
        arr[1], arr[i] = arr[i], arr[1]
        Adjustdown2(arr,1,i-1)
        i -= 1
    result.append(arr[1])
    return result
                
        
        
        

if __name__ == "__main__":
    test = [53,17,78,9,45,65,87,32]
    test2 = [51,2,65,3,6,5,86,15,12,7,24]
    print(SelectSort(test)[::-1])
    print(HeapSort(test))   
    print(SelectSort(test2)[::-1])
    print(HeapSort(test2)) 
    
    print(SelectSort(test))
    print(HeapSort2(test))   
    print(SelectSort(test2))
    print(HeapSort2(test2)) 
    
    
