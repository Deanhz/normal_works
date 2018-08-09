# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 20:30:19 2018

@author: Dean
"""

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

def show(head):
    if not head or not head.next:
        return head
    p = head.next
    while(p):
        print(p.value,end=" ")
        p = p.next
    print("\n")

def resign(stack,left,right):
    head = stack.pop()
    if left:
        left.next = head
    R = head
    while(stack):
        node = stack.pop()
        R.next = node
        R = node
    R.next = right
    return head,R

def reverseKNodes(head, k):#利用栈，每到K个就逆转弹出栈重新链接链表。
    if not head or not head.next:
        return head
    if k <= 1:
        return head
    stack = []
    p = head.next
    i = 0
    pre = head
    while(p):
        i += 1
        stack.append(p)
        tmp = p.next
        p = p.next
        if i == k:
            i = 0
            first,last = resign(stack,pre,tmp)
            pre = last
    return head

def resign2(left,start,end,right):
    p = start
    left.next = None
    while(p!=right):
        tmp = p.next
        p.next = left.next
        left.next = p
        p = tmp
    start.next = right
    return end,start
        


def reverseKNodes2(head, k):
    if not head or not head.next:
        return head
    if k < 2:
        return head
    i = 0
    pre = head
    p = pre.next
    while(p):
        i += 1
        tmp = p.next
        if i == k:
            i = 0
            start = pre.next
#            print(start.value)
            print(pre.value,start.value,p.value)
            first,last = resign2(pre,start,p,tmp)
            pre = last
        p = tmp
    return head

if __name__ == "__main__":
    data = [1,2,3,4,5,6,7,8,9]
    head = Node()
    R = head
    for i in data:
        node = Node(i)
        R.next = node
        R = node
    R.next = None
    show(head)
#    newhead = reverseKNodes(head,3)
#    show(newhead)
    newhead2 = reverseKNodes2(head,3)
    show(newhead2)
    
    
    
    
    
    
    
    
    
    
    
    
    