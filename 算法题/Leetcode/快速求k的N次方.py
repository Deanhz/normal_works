# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 15:37:07 2018

@author: Dean
给定k和n，请返回k的n次方。时间复杂度O(logN)
"""

def getPower(k,N):
    tmp = k
    result = 1
    if N == 0:
        return 1
    if N == 1:
        return k
    while(N>0):
        if N&1 !=0:
            result = result * tmp
        tmp = tmp * tmp
        N = N >>1
    return result

if __name__ == "__main__":
    k = 10
    N = 6
    print(k**N)
    print(getPower(k,N))

