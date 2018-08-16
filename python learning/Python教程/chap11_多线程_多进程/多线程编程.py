# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 17:39:26 2018

@author: user
"""
import threading
import time

def get_detail_html(url):  # 爬取列表页的URL
    print("get detail html start!\n")
    time.sleep(2)
    print("get detail html end!\n")

def get_detail_url(url):  # 爬取URL详情页
    print("get detail url start!\n")
    time.sleep(4)
    print("get detail url end!\n")
    

if __name__== "__main__":
    start_time = time.time()
    t1 = threading.Thread(target=get_detail_html, args=("",))
    t2 = threading.Thread(target=get_detail_url, args=("",))
    t1.start()
    t2.start()
    t1.join()  # 这里的join必须要加，如果不加的话，主线程不阻塞，相当于主线程和两个线程都是并行，最后输出的时间就是0。
    t2.join()
    end_time = time.time()
    print("total time:", end_time - start_time)
    