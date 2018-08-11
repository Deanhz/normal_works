# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 21:47:50 2018

@author: Dean
2 medium 
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
总结：
不难，但是忘记了一种情况，见注释。同时也要注意整除符号不要写错。
"""
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        c = 0
        head = ListNode(None)
        r = head
        while(l1 and l2):
            cum = l1.val + l2.val + c
            c = cum // 10
            s = cum % 10
            node = ListNode(s)
            r.next = node
            r = node
            l1 = l1.next
            l2 = l2.next
        l3 = l2 if l2 else l1
        while(l3):
            cum = l3.val + c
            c = cum // 10
            s = cum % 10
            node = ListNode(s)
            r.next = node
            r = node
            l3 = l3.next
        if c!=0:#忘记了这种情况,有进位。比如 5+5=10,虽然l1和l2长度都是1，但是有进位1,不要忘掉。
            r.next = ListNode(1)
        return head.next
    
def create_list(data):
    head = ListNode(data[0])
    r = head
    for d in data[1:]:
        node = ListNode(d)
        r.next = node
        r = node
    r.next = None
    return head
def show(l):
    while(l):
        print(l.val)
        l = l.next
if __name__ == "__main__":
    l1_data = [2,4,3]
    l2_data = [5,6,4]
    l1 = create_list(l1_data)
    l2 = create_list(l2_data)
    l3 = Solution().addTwoNumbers(l1,l2)
#    print(l3)
    show(l3)
            
            
            
            
        
        
        
            
            
            
            
            
