# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 21:00:02 2018

@author: Dean
p251
"""

def replace(str1, From, to):
    if From not in str1:
        return str1
    match = 0
    n1 = len(str1)
    n2 = len(From)
    str1 = list(str1)
    #手动实现了把str1中from替换成特殊字符^
    for i in range(n1):
        if str1[i] == From[match]:
            match += 1
            if match == n2:
                for j in range(i-n2+1,i+1):
                    str1[j] = "^"
                match = 0
        else:
            if str1[i] == From[0]:
                match =  1
            else:
                match = 0
    #把str1中的^替换成to
    result = []
    for i in range(n1):
        if str1[i] != "^":
            result.append(str1[i])
        if str1[i] == "^" and (i==0 or str1[i-1]!="^"):
            result = result + list(to)
    return "".join(result)
    
    
if __name__ == "__main__":
    test = "123abcabctabc"
    print(replace(test,"abc","X"))
    print(replace("123abc","abc","4567"))
    print(replace("123","abc","X"))
               
            
                

