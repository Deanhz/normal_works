# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 21:07:34 2018

@author: Dean
"""

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

def show(head):
    p = head.next
    while(p):
        print(p.value)
        p = p.next
        
def reversePart(head,From,To):
    if not head or not head.next:
        return head
    p = head.next
    N = 0
    fPre = None #保存From的前一个节点
    tPos = None #保存To的后一个节点
    while(p):
        N += 1
        if N  == From -1 :
            fPre = p
        if N == To + 1:
            tPos = p
        p = p.next
    if not fPre: #如果为空，此时From == 1
        fPre = head
    if (From < 1 or From > To or To >N):
        return head
    p = fPre.next
    fPre.next = tPos
    while(p != tPos):
        tmp = p.next
        p.next = fPre.next
        fPre.next = p
        p = tmp
    return head

head = Node()
R = head
for i in range(1,10):
    Node_i = Node(i)
    R.next = Node_i
    R = Node_i
R.next = None

show(head)
head = reversePart(head,1,5)
print("\n")
show(head)



        