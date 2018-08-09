# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 15:30:04 2018

@author: Dean
"""
#关键思想，将要排序的栈为stack,辅助栈为stack1,不断从stack弹出元素，从辅助栈
#找到合适的位置，把元素放到合适的位置，保证辅助栈为有序。直到stack为空，辅助栈已经
#全部有序，此时把元素逐一加入到stack，stack则为有序(逆序)。
def soreByStack(stack):
    if len(stack) <2 :
        return stack
    stack1 = []
    while(stack):
        cur = stack.pop()
        while(stack1 and stack1[-1] < cur):
            stack.append(stack1.pop())
        stack1.append(cur)
    while(stack1):
        stack.append(stack1.pop())
    return stack

if __name__ == "__main__":
    data = [5,1,4,2,7,3]
    print(soreByStack(data))