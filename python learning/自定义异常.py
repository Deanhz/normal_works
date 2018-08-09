# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 15:55:14 2018

@author: Dean
"""


class DatabaseException(Exception):
    def __init__(self, err="数据库错误"):
        self.errorInfo = err
        super().__init__(self, err)
    def __str__(self):
        return self.errorInfo
     
try:
    raise DatabaseException()
except DatabaseException as e:
    print(e)