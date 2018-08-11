import numpy as np

'''
83 easy
2017.10.30
Given a sorted linked list, delete all duplicates such that each element appear only once.
For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):  # by me
        '''
        :type head: ListNode
        :rtype:ListNode
        '''
        if not head:
            return head

        if head.next is None:
            return head
        curNode = head
        while(curNode):
            nextNode = curNode.next
            if not nextNode:
                break
            while(nextNode and nextNode.val == curNode.val):
                nextNode = nextNode.next
            curNode.next = nextNode
            curNode = nextNode
        return head

    def deleteDuplicates2(self, head):  # best
        if not head or not head.next:
            return head
        pre, curr = head, head.next
        while curr:
            if curr.val == pre.val:
                pre.next = curr.next
                curr = curr.next
            else:
                pre = curr
                curr = curr.next
        return head


def create(l):
    head = ListNode(l[0])
    curNode = head
    for i in l[1:]:
        curNode.next = ListNode(i)
        curNode = curNode.next
    return head


def display(head):
    while(head):
        print(head.val)
        head = head.next


if __name__ == '__main__':
    data = [1, 1, 2, 3, 3]
    linkedList = create(data)
    display(linkedList)
    result = Solution().deleteDuplicates(linkedList)
    display(result)
