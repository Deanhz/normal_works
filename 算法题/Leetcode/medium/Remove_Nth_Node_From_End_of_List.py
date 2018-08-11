# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 21:04:21 2018

@author: Dean
重要!题目看似简单，自己写的提交有错误。这里需要自己添加头结点，然后返回head.next。
19 medium 需要自己添加头结点
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

"""

def create(data):
    head = ListNode(None)
    R = head
    for i in data:
        node = ListNode(i)
        R.next = node
        R = node
    R.next = None
    return head

def show(head):
    if not head or not head.next:
        return head
    p = head.next
    while(p):
        print(p.val,end=" ")
        p = p.next
    print("\n")


class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n): # 遍历两遍
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        first = head
        while(first):
            length += 1
            first = first.next
        k = length - n
        p = dummy
        while(k):
            p = p.next
            k -= 1
        q= p.next
        p.next = q.next
        del(q)
        return dummy.next
    def removeNthFromEnd2(self, head, n): # 遍历一遍
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        p2 = dummy
        while(n):
            p = p.next
            n -= 1
        while(p.next):
            p = p.next
            p2 = p2.next
        q = p2.next
        p2.next = q.next
        del(q)
        return dummy.next
        
            
            
        
        

if __name__ == '__main__':
    data = [1,2,3,4,5]
    head = create(data)
    head2 = Solution().removeNthFromEnd2(head,2)
    show(head2)
    