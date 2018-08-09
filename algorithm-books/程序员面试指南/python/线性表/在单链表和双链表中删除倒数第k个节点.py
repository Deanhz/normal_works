# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 19:57:47 2018

@author: Dean
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next= None

def removeLastKthNode(head,lastK):
    if (not head or lastK < 1)：:
        return head
    cur = head
    i = 0
    while(cur.next):#第一次遍历求出链表的长度
        i += 1
    N = i
    if N <lastK: #如果没有倒数第K个链表，直接返回
        return head
    if N == lastK:#倒数第K个节点就是头结点
        q = head
        head = head.next
        del(q)
        return head
    cur = head
    i = 0
    while(i < N - lastK):#第N-lastK个节点是，lastK节点的前一个节点
        cur = cur.next
    q = cur.next
    cur.next = q.next
    del(q)
    return head

class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.last = None
        
def removeLastKthNode2(head,lastK):
    if (not head or lastK < 1)：:
        return head
    cur = head
    i = 0
    while(cur.next):#第一次遍历求出链表的长度
        i += 1
    N = i
    if N <lastK: #如果没有倒数第K个链表，直接返回
        return head
    if N == lastK:#倒数第K个节点就是头结点
        q = head
        head = head.next
        del(q)
        return head
    cur = head
    i = 0
    while(i < N - lastK):#第N-lastK个节点是，lastK节点的前一个节点
        cur = cur.next
    q = cur.next
    cur.next = q.next
    q.next.last = cur
    del(q)
    return head
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    