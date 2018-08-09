# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 09:31:42 2018

@author: Dean
"""

#m进制转化为n进制
def m_to_n(num,m,n):
    #m to 10
    w = 1
    res_10 = 0
    for i in str(num)[::-1]:
        res_10 += int(i) * w
        w = w * m
    
    #10 to n
    res_2 = []
    while(res_10>0):
        res_2.insert(0,str(res_10 % n))
        res_10 = res_10 // n
    res_2 = "".join(res_2)
    return res_2

if __name__ == "__main__":
    print(m_to_n("10",16,2))
    print(bin(int("10",base=16)))