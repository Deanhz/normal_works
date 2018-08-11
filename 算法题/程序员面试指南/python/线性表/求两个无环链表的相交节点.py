# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 10:02:29 2018

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

def GetIntersect(head1,head2): 
    if not head1 or not head1.next:
        return None
    if not head2 or not head2.next:
        return None
    len1 =0
    len2 = 0
    p1 = head1
    p2 = head2
    while(p1.next):
        len1 += 1
        p1 = p1.next
    while(p2.next):
        len2 += 1
        p2 = p2.next
    if p1 != p2:
        return None
    cur1 = head1 if len1 > len2 else head2
    k = abs(len1 - len2)
    while(k > 0):
        cur1 = cur1.next
        k -= 1
    cur2 = head2 if len1 > len2 else head1
    while(cur1 != cur2 ):
        cur1 = cur1.next
        cur2 = cur2.next
    return cur1

if __name__ == "__main__":
    data = [1,2,3,4,5,6,7,8,9]
    head1 = Node()
    head2 = Node()
    r1 = head1
    r2 = head2
    intersect_node = None
    for i in data:
        node = Node(i)
        if i == 5:
            intersect_node = node
        r1.next = node
        r1 = node
    node = Node(4)
    r2.next = node
    node.next = intersect_node
    show(head1)
    show(head2)
    
    get_intersect_node = GetIntersect(head1,head2)
    print(get_intersect_node.value)
    
    
    
    
    
    
    
    
    
