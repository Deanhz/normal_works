# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 19:52:38 2018

@author: Dean
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def printCommonPart(head1,head2):
    print("Common part: ")
    while(head1 and head2):
        if(head1.value <head2.value):
            head1 = head1.next
        elif (head1.value >head2.value):
            head2 = head2.next
        else:
            print(head1.value)
            head1 = head1.value
            head2 = head2.value
