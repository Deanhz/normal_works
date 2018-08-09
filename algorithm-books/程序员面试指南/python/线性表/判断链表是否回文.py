# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 09:20:45 2018

@author: Dean
"""

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

def show(head):
    p = head.next
    while(p):
        print(p.value,end=" ")
        p = p.next
    print("")

def isPalindrome1(head): #利用栈保存所有节点值，时间复杂度O(N),空间复杂度O(N)
    if not head or not head.next:
        return True
    stack = []
    p = head.next
    while(p):
        stack.append(p.value)
        p = p.next
    p = head.next
    while(stack):
        if p.value != stack.pop():
            return False
        p = p.next
    return True

def isPalindrome2(head):# 利用栈保存右半部分的值，时间复杂度O(N),空间复杂度O(N/2)
    if not head or not head.next:
        return True
    stack = []
    p1 = head.next
    p2 = head.next
    while(p2.next and p2.next.next):#找到中间节点
        p1 = p1.next
        p2 = p2.next.next
    mid = p1 #中间节点
    p = mid.next #从中间节点的右节点开始入栈。
    while(p):
        stack.append(p.value)
        p = p.next
    p = head.next
    while(stack):
        if p.value != stack.pop():
            return False
        p = p.next
    return True

def isPalindrome3(head): #反转右半部分链表，时间复杂度O(N),空间复杂度O(1)
    if not head or not head.next:
        return True
    p1 = head.next
    p2 = head.next
    while(p2.next and p2.next.next):
        p1 = p1.next
        p2 = p2.next.next
    mid = p1
    p = mid.next
    mid.next = None
    while(p): #反转右半部分链表
        tmp = p.next
        p.next = mid.next
        mid.next = p
        p = tmp
    #开始比较
    p = head.next
    q = mid.next 
    while(q):
        if q.value != p.value:
            return False
        q = q.next
        p = p.next
    #恢复，再一次右半部分反转
    p = mid.next
    mid.next = None
    while(p):
        tmp = p.next
        p.next = mid.next
        mid.next = p
        p = tmp
    show(head)
    
    return True
    
    


if __name__ == "__main__":
    data = [1,2,3,4,4,3,2,1]
    head = Node()
    R = head
    for i in data:
        node_i = Node(i)
        R.next = node_i
        R = node_i
    R.next = None
    show(head)
    print(isPalindrome1(head))
    print(isPalindrome2(head))
    print(isPalindrome3(head))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        