# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 14:55:53 2018

@author: Dean
"""

def getMaxLength1(arr,k):#时间复杂度O(N*N)
    if not arr:
        return 0
    data = arr.copy()
    length = len(data)
    maxLen = 0
    for left in range(length):
        for right in range(length):
            sumVal = sum(data[left:right+1])
            if sumVal == k:
                if right - left + 1 >maxLen:
                    maxLen = right - left + 1
            else:
                continue
    return maxLen

def getMaxLength2(arr, k):
    if not arr:
        return 0
    s = {} #s[i]表示从0到i的元素累加和
    dic = {0:-1} #表示sum=key最早出现时，下标是value
    length = len(arr)
    maxLen = 0
    for i in range(length):
        s[i] = sum(arr[:i+1])
        if not dic.get(s[i],None):
            dic[s[i]] = i
        if (s[i] - k) in dic:
            maxLen = max(maxLen,i - dic[s[i]-k])
    return maxLen
    


if __name__ == "__main__":
    data = [-1,-2,-3,0,1,2,3,4]
    print(getMaxLength1(data,-3))
    print(getMaxLength2(data,-3))
        
    