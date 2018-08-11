# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 14:24:26 2018

@author: Dean
"""

def getMaxLength1(arr, k):#时间复杂度O(N*N)
    if not arr or k<0:
        return 0
    maxLen = 0
    length = len(arr)
    for left in range(length):
        for right in range(length):
            sumVal = sum(arr[left:right+1])
            if sumVal == k:
                if right - left + 1 >maxLen:
                    maxLen = right - left + 1
            elif sumVal > k:
                break
            else:
                continue
    return maxLen

def getMaxLength2(arr, k):#时间复杂度O(N)
    if not arr or k<0:
        return 0
    length = len(arr)
    left = 0
    right = 0
    sumVal = arr[0]
    maxLen = 0
    while(right < length):
        sumVal = sum(arr[left:right+1])
        if sumVal == k:
            if right - left + 1> maxLen:
                maxLen = right - left + 1
            sumVal = sumVal - arr[left]
            left += 1
        elif sumVal < k:
            right += 1
        else:
            sumVal = sumVal - arr[left]
            left += 1
    return maxLen
            
            

if __name__ == "__main__":
    data = [1,2,1,1,1,1,3,2,1,1,2,3]
    print(getMaxLength1(data,4))
    print(getMaxLength2(data,4))
    
                
                    
    