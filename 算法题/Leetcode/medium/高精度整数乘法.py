# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 19:23:54 2018

@author: Dean
参考链接：
http://www.cnblogs.com/TenosDoIt/p/3735309.html
https://www.cnblogs.com/springfor/p/3889706.html
"""

def func(str1, str2):
    if str1 == "0" or str2 == "0":
        return "0"
    n1 = len(str1)
    n2 = len(str2)
    num1 = str1[::-1]
    num2 = str2[::-1]
    tmp = [0 for i in range(n1+n2)]#保存未进位之前的临时计算结果
    result = []
    #计算临时结果
    for i in range(n1):
        for j in range(n2):
            tmp[i+j] += int(num1[i]) * int(num2[j])
    #计算进位后的结果
    c = 0
    for i in range(n1+n2):
        tmp[i] += c
        c = tmp[i] // 10
        result.insert(0,str(tmp[i]%10))
    #删除结果前面的0
    while(result and result[0] == "0"):
        result.pop(0)
    return "".join(result)
    
            
if __name__ == '__main__':
    result = func("280","750")
    print(result)