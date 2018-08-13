# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 20:44:53 2018

@author: Dean
"""

class Group:
    def __init__(self, name, staffs):
        self.name = name
        self.staffs = staffs
    
    def __getitem__(self, item):
        cls = type(self)  # 获取当前类
        if isinstance(item, slice):
            return cls(name=self.name, staffs=self.staffs[item])  # 交给staffs即可。
        elif isinstance(item, int):
            return cls(name=self.name, staffs=[self.staffs[item]]) # 注意这个地方传递需要是list
    
    def __len__(self):
        return len(self.staffs)
    
    def __iter__(self):
        return iter(self.staffs)
    
    def __contains__(self, item):
        return True if item in self.staffs else False
    
    def __setitem__(self, index, item):
        self.staffs[index] = item
    
    def __delitem__(self, index):
        del(self.staffs[index])
    
    def __reversed__(self):
        self.staffs.reverse()
    1
g1 = Group("g1", ["xiaoming", "xiaolee", "xiaoding"])
print(g1[:2].staffs)
reversed(g1)
print(g1.staffs)
print("xiaoding" in g1)
print([i for i in g1])



