# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 13:58:29 2018

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

def delete_repeat(head):
    if not head or not head.next:
        return head
    pre = head
    p = head.next
    dic = {}
    while(p):
        value = p.value
        tmp = p.next
        dic[value] = dic.get(value,0) +1
        if dic[value] != 1: #注意pre的变化！！！！！
            pre.next = p.next
            p = tmp
        else:
            pre = p
            p = tmp
    return head

if __name__ == "__main__":
    data = [1,2,3,4,5,6,7,8,9,3,5,6,9]
    head = Node()
    R = head
    for i in data:
        node = Node(i)
        R.next = node
        R = node
    R.next = None
    show(head)
    delete_repeat(head)
    show(head)