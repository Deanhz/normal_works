# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 22:01:25 2018

@author: Dean
p245
"""

def removeKzeros(str1, k): 
    if not str1 or k < 0:
        return str1
    n = len(str1)
    result = list(str1)
    count = 0
    start = -1
    for i in range(n):
        c = result[i]
        if c == "0":
            start = i if start == -1 else start
            count += 1
        else:
            if count == k:
                while(k>0):
                    result[start] = ""
                    start += 1
                    k -= 1
            count = 0
            start = -1
    if count == k:
        while(k > 0):
            result[start] = ""
            k -= 1
            start += 1
    return "".join(result)
          
if __name__ == "__main__" :
    str1 = "A0000B000"
    str2 = "A00B"
    k = 3
    print(removeKzeros(str1,3))
    print(removeKzeros(str2,2))
