# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 22:10:39 2018

@author: user
"""

def BucketSort(arr):  # 时间复杂度O(m+n), 桶的数目 + 数的个数
    if not arr:
        return arr
    res = []
    Max = max(arr)
    Min = min(arr)
    abs_max = max(-Min, Max)
    Bucket = [0 for i in range(abs_max+1)]  # 0表示桶内没有数，1表示桶内有数
    book = [0 for i in range(abs_max+1)]  # 标志桶内正数的数目
    bookN = [0 for i in range(abs_max+1)]  # 标志桶内负数的数目
    for num in arr:  # 把每个数分配到每个桶内，绝对值相同的正数和负数我们放在同一个桶内，使用标志位区分
        if num < 0:
            Bucket[-num] = 1
            bookN[-num] += 1
        else:
            Bucket[num] = 1
            book[num] += 1
    for i in range(abs_max)[::-1]:  # 先输出负数，因为是负数，所以按照桶序号的从大到小
        if Bucket[i] == 1:
            for j in range(bookN[i]):
                res.append(-i)
    for i in range(abs_max):
        if Bucket[i] == 1:
            for j in range(book[i]):
                res.append(i)
    return res


if __name__ == "__main__":
    test = [-5, 2, 5, 6, 7, 2, -7, -5, 8, 0]
    print(BucketSort(test))
        
    
    