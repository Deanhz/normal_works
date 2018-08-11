# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 10:46:48 2018

@author: Dean
"""

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.rand = None

def show(head):
    if not head or not head.next:
        return head
    p = head.next
    while(p):
        print(p.value,end=" ")
        if p.rand:
            print(p.rand.value)
        p = p.next
    print("\n")
    
def copyListWithRand1(head):#使用map，时间复杂度和空间复杂度都是O(N)
    if not head or not head.next:
        return head
    dic = {}
    p = head
    while(p):
        copyNode = Node(p.value)
        dic[p] = copyNode
        p = p.next
    p = head
    while(p):
        dic[p].next = dic.get(p.next,None)
        dic[p].rand = dic.get(p.rand,None)
        p = p.next
    return dic[head]

def copyListWithRand2(head): #不适用map,时间复杂度O(N)，空间复杂度O(1)
    #见书P58
    if not head or not head.next:
        return head
    #连接链表，把copyNode放在节点后面
    p = head
    while(p):
        copyNode = Node(p.value)
        tmp = p.next
        copyNode.next = p.next
        p.next = copyNode
        p = tmp
    #链接copyNode的rand节点
    p = head
    while(p):
        copyNode = p.next
        if p.rand:
            copyNode.rand = p.rand.next
        p = copyNode.next
    #拆分链表 [留意一下]
    head2 = head.next
    p = head
    while(p):
        tmp = p.next.next
        copyNode = p.next
        p.next = tmp
        copyNode.next = tmp.next if tmp else None
        p = tmp
    return head2
    
        

if __name__ == "__main__":
    data = list(range(1,10))
    head = Node()
    R = head
    for i in data:
        node_i = Node(i)
        R.next = node_i
        R = node_i
    p = head
    while(p):
        if p.next:
            p.rand = p.next.next
        p = p.next
    show(head)
    head2 = copyListWithRand1(head)
    show(head2)
    head3 = copyListWithRand2(head)
    show(head3)
    
        
        
        
        
        
        
        
        
        
        
        
        
        