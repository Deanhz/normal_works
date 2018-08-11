# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 13:53:58 2018

@author: Dean
"""

def func(str1, str2):
    n1 = len(str1)
    n2 = len(str2)
    num1 = str1[::-1]
    num2 = str2[::-1]
    result = []
    min_len = num1
    max_len = num2
    if n2 < n1:
        min_len = num2
        max_len = num1
    t = 0
    c = 0
    for i in range(max(n1,n2)):
        t = 0
        if i < min(n1,n2):
           t = int(min_len[i]) + int(max_len[i]) + c
        else:
            t = int(max_len[i]) + c
        c = t // 10
        result.append(str(t%10))
    if c!=0:
        result.append(str(c))
    return "".join(result[::-1])

if __name__ == "__main__":
    s1 = '99999'
    s2 = '99999999'
    result = func(s1,s2)
    print(result)