# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 23:00:16 2018

@author: Dean
24 medium 链表
Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.
"""
def show(head):
    if not head or not head.next:
        return head
    p = head.next
    while(p):
        print(p.val,end=" ")
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


 class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        p1 = head
        p2 = head.next
        if not p2:
            return head
        while(p1 and p2):
            tmp = p2.next
            p2.next = p1
            pre.next = p2
            p1.next = tmp
            pre = p1
            p1 = tmp
            if not tmp: #注意需要判断tmp是否为空
                p2 = None
            else:
                p2 = tmp.next
        return dummy.next
    
if __name__ == "__main__":
    data = [1,2,3,4]
    head = 
        