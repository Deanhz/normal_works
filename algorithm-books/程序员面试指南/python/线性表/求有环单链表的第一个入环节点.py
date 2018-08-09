# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 09:41:50 2018

@author: Dean
"""

#判断单链表是否有环，并返回第一个进入环的节点
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

def show(head):
    if not head or not head.next:
        return head
    p = head.next
    i = 1
    while(p):
        print(p.value,end=" ")
        p = p.next
        i += 1
        if i>=30:
            break
    print("\n")

def getFirstLoopNode(head):
    if not head or not head.next or not head.next.next:
        print(1)
        return None
    p1 = head.next
    p2 = head.next.next
    while(p1 != p2):
        if not p2.next or not p2.next.next:
            return None
        p1 = p1.next
        p2 = p2.next.next
    p2 = head
    while(p1 != p2):
        p1 = p1.next
        p2 = p2.next
    return p1

if __name__ == "__main__":
    data = [1,2,3,4,5,6,7,8,9,10]
    head = Node()
    r = head
    firstLoop = None
    for i in data:
        node = Node(i)
        if i == 4:
            firstLoop = node
        r.next = node
        r = node
    r.next = firstLoop
    show(head)
    get_firstLoop = getFirstLoopNode(head)
    print(get_firstLoop.value)
    
    
    
    