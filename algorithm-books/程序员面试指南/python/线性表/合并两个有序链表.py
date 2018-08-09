# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 14:31:47 2018

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
def create(data):
    head = Node()
    R = head
    for i in data:
        node = Node(i)
        R.next = node
        R = node
    R.next = None
    return head
    
def combine(head1,head2):
    if not head1 or not head1.next:
        return head2
    if not head2 or not head2.next:
        return head1
    p1 = head1.next
    p2 = head2.next
    head1.next = None
    R = head1
    while(p1 and p2):
        if p1.value <= p2.value:
            R.next = p1
            R = p1
            p1 = p1.next
        else:
            R.next = p2
            R = p2
            p2 = p2.next
    while(p1):
        R.next = p1
        R = p1
        p1 = p1.next
    while(p2):
        R.next = p2
        R = p2
        p2 = p2.next
    return head1

if __name__ == "__main__":
    data1 = [0,2,3,7]
    data2 = [1,3,5,7,9]
    head1 = create(data1)
    head2 = create(data2)
    show(head1)
    show(head2)
    head3 = combine(head1,head2)
    show(head3)
    
    
    
    
    
    
    
    
    
    
    
    
    

