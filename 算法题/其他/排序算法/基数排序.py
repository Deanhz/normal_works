# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 21:24:08 2018

@author: user
"""

def RadixSort(arr, d):
    if not arr:
        return arr
    for k in range(d):  # d轮排序, 每一轮是一个数位
        s = [[] for i in range(10)]  # 因为每一个数字都是0-9, 故建立10个桶
        for num in arr: 
            index = num // (10**k) % 10  # 分配，根据该数位把该number放入对应的桶中
            s[index].append(num)
        arr = [j for i in s for j in i]  # 收集
    return arr



if __name__ == "__main__":
    data = [720, 329, 457, 657, 839, 436, 355]
    print(RadixSort(data, 3))