# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 23:16:13 2018

@author: Dean
"""
import threading
'''
对话
天猫精灵：小爱同学
小爱：在
天猫精灵：我们来对古诗吧
小爱：好啊
天猫精灵：我住长江头
小爱：君住长江尾
天猫精灵：日日思君不见君
小爱：共饮长江水
'''

TM = ["小爱同学", "我们来对古诗吧", "我住长江头", "日日思君不见君"]
XA = ["在", "好啊", "君住长江尾", "共饮长江水"]


class XiaoAi(threading.Thread):
    def __init__(self, condition):
        super().__init__(name="小爱")
        self.cond = condition
    
    def run(self):
        with self.cond:
            for s in XA:
                self.cond.wait()
                print("{}: {}\n".format(self.name, s))
                self.cond.notify()
        

class TianMao(threading.Thread):
    def __init__(self, condition):
        super().__init__(name="天猫精灵")
        self.cond = condition
    
    def run(self):
        with self.cond:
            for s in TM:
                print("{}: {}\n".format(self.name, s))
                self.cond.notify()
                self.cond.wait()
            
            
if __name__ == "__main__":
    cond = threading.Condition()
    xiaoai = XiaoAi(cond)
    tianmao = TianMao(cond)
    # 启动顺序很重要
    # 在with condtion之后才能调用wait()和notify()
    xiaoai.start()
    tianmao.start()
           
            
            
    
    
    
    