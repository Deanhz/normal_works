# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 11:18:19 2018

@author: Dean
"""
#见书P66
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

def show(head):
    if not head or not head.next:
        return head
    p = head.next
    i = 1
    while(p):
        print(p.value,end=" ")
        p = p.next
        i += 1
        if i>=30:
            break
    print("\n")
def getFirstLoopNode(head):
    if not head or not head.next or not head.next.next:
        print(1)
        return None
    p1 = head.next
    p2 = head.next.next
    while(p1 != p2):
        if not p2.next or not p2.next.next:
            return None
        p1 = p1.next
        p2 = p2.next.next
    p2 = head
    while(p1 != p2):
        p1 = p1.next
        p2 = p2.next
    return p1
    
def GetIntersect_Loop(head1,head2):
    if not head1 or not head1.next:
        return None
    if not head2 or not head2.next:
        return None
    loop1 = getFirstLoopNode(head1)
    loop2 = getFirstLoopNode(head2)
    
    if loop1 == loop2:#若相等，则公共节点在入环之前
        p1 = head1
        p2 = head2
        len1 = 0
        len2 = 0
        while(p1.next != loop1):
            len1 += 1
            p1 = p1.next
        while(p2.next != loop2):
            len2 += 1
            p2 = p2.next
        cur1 = head1 if len1 > len2 else head2
        cur2 = head2 if len1 > len2 else head1
        n = abs(len1 - len2)
        while(n > 0):
            cur1 = cur1.next
            n -= 1
        while(cur1 != cur2):
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1
    else:#若不相等，判断公共节点是否在环内部
        cur1 = loop1.next
        while(cur1 != loop1):
            if cur1 == loop2:#如果找到了loop2，说明是同一个环，此时loop1和loop2都是公共节点。否则，不是同一个环，没有公共结点。
                return loop1
            cur1 = cur1.next
        return None

if __name__ == "__main__":
    data = [1,2,3,4,5,6,7,8,9,10]
    head = Node()
    r = head
    firstLoop = None
    secondLoop = None
    for i in data:
        node = Node(i)
        if i == 4:
            firstLoop = node
        if i == 5:
            secondLoop = node
        r.next = node
        r = node
    r.next = firstLoop
    
    head2 = Node()
    r2 = head2
    node = Node(4)
    r2.next = node
    r2 = node
    r2.next = secondLoop
    
    show(head)
    show(head2)
    
    Intersect_node = GetIntersect_Loop(head,head2)
    print(Intersect_node.value)
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    