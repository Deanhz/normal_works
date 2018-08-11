# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 14:08:26 2018

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
    i = 1
    while(p):
        print(p.value,end=" ")
        p = p.next
        i += 1
        if i>=30:
            break
    print("\n")
    
def insertWithLoop(head,value):
    if not head or not head.next:
        return head
    pre = head
    p = head.next
    while(p):
        if p.value >= value:
            node = Node(value)
            node.next = p
            pre.next = node
            return head
        pre = p
        p = p.next
    return head

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
    head2 = insertWithLoop(head,5.5)
    show(head2)