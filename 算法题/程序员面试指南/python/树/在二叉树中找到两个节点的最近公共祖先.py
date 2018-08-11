# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 15:28:07 2018

@author: Dean
"""

class Node:
    def __init__(self,value=None):
        self.value = value
        self.left = None
        self.right = None

def createByPreInOder(preOrder,InOrder):
    if not preOrder or not InOrder:
        return None
    length = len(preOrder)
    tree = Node(preOrder[0])
    mid = 0
    for i in range(length):
        if InOrder[i] == preOrder[0]:
            mid = i
            break
    lenL = mid
    tree.left = createByPreInOder(preOrder[1:lenL+1],InOrder[:mid])
    tree.right = createByPreInOder(preOrder[lenL+1:],InOrder[mid+1:])
    return tree

def posOrderUnRecur(tree,o1,o1_ancestor,o2,o2_ancerstor):
    if not tree:
        return tree
    stack = []
    stack.append(tree)
    cur = None
    last = None
    while(stack):
        cur = stack[-1]
        if(cur.left and last!=cur.left and last!=cur.right):
            stack.append(cur.left)
        elif(cur.right and last!=cur.right):
            stack.append(cur.right)
        else:
            if cur.value == o1:
                o1_ancestor[:] = stack #注意使用截取
            if cur.value  == o2:
                o2_ancerstor[:] = stack
            stack.pop()
            last = cur

def getAncestor(head,o1,o2): # ByMe 首先通过非递归后续遍历找到各自的祖先序列。然后再找最近的公共祖先。
    if not head or head == o1 or head == o2:
        return head
    o1_ancestor = []
    o2_ancestor = []
    posOrderUnRecur(head,o1,o1_ancestor,o2,o2_ancestor)
    len1 = len(o1_ancestor)
    len2 = len(o2_ancestor)
    min_len = min(len1,len2)
    if len1 > len2:
        o1_ancestor = o1_ancestor[:min_len]
    else:
        o2_ancestor = o2_ancestor[:min_len]
    for i in range(min_len)[::-1]:
        if o1_ancestor[i] == o2_ancestor[i]:
            return o1_ancestor[i]

#面试指南
def getAncestor2(head,o1,o2): #精巧
    if not head or head.value == o1 or head.value == o2:
        return head
    left = getAncestor2(head.left,o1,o2)
    right = getAncestor2(head.right,o1,o2)
    if left and right:
        return head
    if left:
        return left
    else:
        return right

#进阶问题，如果查询操作非常频繁，想法让降低查询时间复杂度

#方法一，建立每个节点对应父节点信息的哈希表
#建立记录的时间复杂度O(N)、空间复杂度O(N)
#查询时间复杂度O(h),h为树的高度
class Record1:
    def __init__(self,head):
        self.map = {head.value:None}
        self.setMap(head)
    def setMap(self,tree):
        if not tree:
            return
        if tree.left:
            self.map[tree.left.value] = tree.value
        if tree.right:
            self.map[tree.right.value] = tree.value
        self.setMap(tree.left)
        self.setMap(tree.right)
    def query(self,o1,o2):
        o1_ancestor = []
        o1_ancestor.append(o1)
        parent = self.map.get(o1,None)
        while(parent is not None):
            o1_ancestor.append(parent)
            parent = self.map.get(parent,None)
        while(o2 not in o1_ancestor):
            o2 = self.map[o2]
        return o2

#方法二，直接建立任意两个节点间的最近公共祖先记录
#任意两个节点之间保存祖先信息，总有(N-1)*N/2条信息，所以建立记录的时间复杂度为O(N^2)
#建立记录的空间复杂度为O(N^2)
#查询时间复杂度O(1)
class Record2:
    def __init__(self, head):
        self.map = {}
        self.initMap(head)
        self.setMap(head)
        
    def initMap(self,head):
        if not head:
            return
        self.map[head.value] = {}
        self.initMap(head.left)
        self.initMap(head.right)
    
    def setMap(self, head):
        if not head:
            return
        #设置以head为公共祖先的子树
        #设置后代节点和head的最近公共祖先为head
        self.headRecord(head.left,head)
        self.headRecord(head.right,head)
        #设置左子树任意节点和右子树任意节点的最近公共祖先为head
        self.subRecord(head)
        #递归调用，设置所有子树
        self.setMap(head.left)
        self.setMap(head.right)
    
    def headRecord(self,n,h):
        if not n:
            return 
        self.map[n.value][h.value] = h.value
        self.headRecord(n.left,h)
        self.headRecord(n.right,h)
    
    def subRecord(self,head):
        if not head:
            return
        self.preLeft(head.left,head.right,head)
        self.subRecord(head.left)
        self.subRecord(head.right)
    
    def preLeft(self,l,r,h):
        if not l:
            return 
        self.preRight(l,r,h)
        self.preLeft(l.left,r,h)
        self.preLeft(l.right,r,h)
    
    def preRight(self,l,r,h):
        if not r:
            return
        self.map[l.value][r.value] = h.value
        self.preLeft(l,r.left,h)
        self.preLeft(l,r.right,h)
    
    def query(self,o1,o2):
        if o1 == o2:
            return o1
        if o1 in self.map:
            if o2 in self.map[o1]:
                return self.map[o1][2]
        if o2 in self.map:
            if o1 in self.map[o2]:
                return self.map[o2][o1]
        return None
        


if __name__ == "__main__":
    preOrder = [1,2,4,5,3,6,7,8]
    InOrder = [4,2,5,1,6,3,8,7]
    tree = createByPreInOder(preOrder,InOrder)
    node = getAncestor(tree,3,8)
    node2 = getAncestor2(tree,3,8)
    print(node.value)
    print(node2.value)
    record1 = Record1(tree)
    print(record1.query(3,8))
    record2 = Record2(tree)
    print(record2.query(3,8))
    
    
    
    
    
    
    
    
    
    
    
    
    
    