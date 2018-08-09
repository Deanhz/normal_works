# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 21:39:07 2018

@author: Dean
"""

def sumStr(str1): # by me
    if not str1:
        return 0
    n = len(str1)
    flag = True #表示符号的正负
    result = 0 #最终结果
    num = 0 #保存当前收集到的数字
    for i in range(n):
        c = str1[i]
        if c == "-":
            flag = False
        if ord(c) >= ord("0") and ord(c) <= ord("9"):
            num = num * 10 + int(c)
        else:
            result += num if flag else -num
            num = 0 # 恢复默认
            flag = True # 恢复默认
    
    if num != 0: # 处理数字在末尾的情况
        result += num if flag else -num
    return result

if __name__ == "__main__":
    str1 = "A1CD2E.33"
    print(sumStr(str1))