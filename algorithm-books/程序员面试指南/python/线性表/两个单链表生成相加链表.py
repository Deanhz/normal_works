# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 08:50:08 2018

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

def addList(head1,head2): #使用栈，分别保存两个链表的逆序，然后从低位到高位相加。还可以把两个链表逆序，再从低位到高位相加。
    if not head1 or not head1.next:
        return head2
    if not head2 or not head2.next:
        return head1
    stack1 = []
    stack2 = []
    p1 = head1.next
    p2 = head2.next
    while(p1):
        stack1.append(p1.value)
        p1 = p1.next
    while(p2):
        stack2.append(p2.value)
        p2 = p2.next
    c = 0
    n1 = 0
    n2 = 0
    pre = None
    while(stack1 or stack2):
        n1 = stack1.pop() if stack1 else 0
        n2 = stack2.pop() if stack2 else 0
        n = n1 + n2 + c
        node = Node(int(n % 10))
        node.next = pre
        pre = node
        c = n / 10
    if c == 1:
        node = Node(1)
        node.next = pre
        pre = node
    head = Node()
    head.next = pre
    return head

if __name__ == "__main__":
    data1 = [9,3,7]
    data2 = [6,3]
    head1 = Node()
    head2 = Node()
    R1 = head1
    R2 = head2
    for i in data1:
        node = Node(i)
        R1.next = node
        R1 = node
    for j in data2:
        node = Node(j)
        R2.next = node
        R2 = node
    head = addList(head1,head2)
    show(head)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
