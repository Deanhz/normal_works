# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 15:38:09 2018

@author: Dean

"""

def func():
    line1 = input().strip().split(" ")
    line2 = input().strip().split(" ")
    line3 = input().strip().split(" ")
    n, k = list(map(int, line1))
    score = list(map(int, line2))
    wake = list(map(int, line3))
    n = len(score)
    res = 0
    max_score = 0
    index = 0
    for i in range(n):
        if wake[i] == 1:
            res += score[i]
            continue
        tmp = sum(score[i:i+k])
        for j in range(i, i+k):
            if j < n and wake[j] == 1:
                tmp -= score[j]
        if tmp > max_score:
            max_score = tmp
            index = i
    for i in range(index, index+k):
        if i >= n:
            break
        if wake[i] == 0:
            res += score[i]
    return res


if __name__ == "__main__":
    print(func())