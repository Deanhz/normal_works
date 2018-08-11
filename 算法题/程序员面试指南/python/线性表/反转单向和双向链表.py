# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 20:41:51 2018

@author: Dean
"""
#使用头插法反转链表
def reverseList1(head):
    if not head:
        return head
    if not head.next:
        return head
    cur = head.next
    head.next = None
    while(cur):
        tmp = cur.next
        cur.next = head.next
        head.next = cur
        cur = tmp
    return head

def reverseList(head):
    if not head:
        return head
    if not head.next:
        return head
    cur = head.next
    head.next = None
    while(cur):
        tmp = cur.next
        cur.next = head.next
        if head.next:
            head.next.last = cur
        head.next = cur
        cur.last = head
        cur = tmp
    return head
