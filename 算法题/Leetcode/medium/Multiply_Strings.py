# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 13:18:17 2018

@author: Dean
"""

class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if int(num1) == 0 or int(num2) == 0:
            return str(0)
        if int(num1) == 1:
            return num2
        if int(num2) == 1:
            return num1
        