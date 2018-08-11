# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 14:44:15 2018

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

def left_right_combine(head):
    if not head or not head.next:
        return head
    p = head.next
    N = 0
    while(p):
        N += 1
        p = p.next
    mid_i = N//2
    i = -1
    p = head.next
    while(p):
        i += 1
        if i == mid_i:
            break
        p = p.next
    mid = p
    p = head.next
    p2 = mid
    head.next = None
    R = head
    i = 0
    
    while(p!=mid and p2): #注意这里的条件！
        if i % 2 == 0:    #这里是用的尾插法。
            tmp = p.next
            R.next = p
            R = p
            p = tmp
        else:
            tmp = p2.next
            R.next = p2
            R = p2
            p2 = tmp
        i += 1
    #下面这些很重要，不能忽略！
    while(p!=mid):
        R.next = p
        R = p
        p = p.next
    while(p2):
        R.next = p2
        R = p2
        p2 = p2.next
    R.next = None
    return head

def left_right_combine2(head):
    if not head or not head.next:
        return head
    if not head.next.next:
        return head
    p = head.next
    q = head.next.next
    while(q.next and q.next.next): #找到左半区最后一个节点，保存在p。
        p = p.next                 #注意这里的条件！
        q = q.next.next
    mid = p.next
    p.next = None
    left = head.next
    right = mid
    while(left.next and right):#这里是把right插入到left之中。
        tmp = right.next
        tmp2 = left.next
        right.next = left.next
        left.next = right
        right = tmp
        left = tmp2
    left.next = right #勿忘！
    return head
        
    


if __name__ == "__main__":
    data = [1,2,3,4,5,6,7,8]
    data2 = [1,2,3,4,5,6,7]
    head1 = create(data)
    head2 = create(data2)
#    head3 = left_right_combine(head1)
#    show(head3)
#    head4 = left_right_combine(head2)
#    show(head4)
    head5 = left_right_combine2(head2)
    show(head5)
        
        
        
        
        