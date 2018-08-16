# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 16:09:56 2018

@author: Dean
"""

def func():
    line1 = input().strip().split(" ")
    line2 = input().strip().split(" ")
    n, k = list(map(int, line1))
    hs = list(map(int, line2))
    if n < 1 or n > 100:
        return
    if k < 1 or k > 1000:
        return
    n = len(hs)
    max_h, min_h = 0, 0
    max_h_ind = -1
    min_h_ind = -1
    moves = []
    min_value = 0
    m = 0
    def find_max_min(hs, n):
        max_h, max_ind = 0, -1
        min_h, min_ind = 9999, -1
        for i in range(n):
            if hs[i] > max_h:
                max_h = hs[i]
                max_ind = i
            if hs[i] < min_h:
                min_h = hs[i]
                min_ind = i
        return max_h, max_ind, min_h, min_ind
    max_h, max_h_ind, min_h, min_h_ind = find_max_min(hs, n)
    while(k > 0):
        if max_h - min_h > 1:
            m += 1
            moves.append([max_h_ind+1, min_h_ind+1])
            hs[max_h_ind] -= 1
            hs[min_h_ind] += 1
            max_h, max_h_ind, min_h, min_h_ind = find_max_min(hs, n)
            k -= 1
        else:
            break
    min_value = max_h - min_h
    print(min_value, m)
    for move in moves:
        print(move[0], move[1])


if __name__ == "__main__":
    func()