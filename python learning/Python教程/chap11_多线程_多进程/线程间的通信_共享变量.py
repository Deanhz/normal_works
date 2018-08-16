# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 18:44:05 2018

@author: user
线程通信方式
1. 共享变量
这是最简单直接的方式。
存在的问题是：共享变量的方式不是线程安全的操作，容易存在问题，不推荐使用。
2. 消息队列
"""

import threading
import time
import variables



def get_detail_url():  # 爬取文章列表页
    while(True):
        print("get detail url start!\n")
        time.sleep(4)
        for i in range(20): # 假设一次性抓取20个url
            variables.detail_url_list.append("http://www.baidu.com/{id}".format(id=i))
        variables.numbers[0] += 20
        print("get detail url end!\n")
        if variables.numbers[0] > 100:  # 爬取数量超过100则退出
            break
    
def get_detail_html():  # 爬取文章详情页
    while(True):
        if variables.detail_url_list:
            url = variables.detail_url_list.pop()
            variables.numbers[1] += 1
            # 爬取详情页
            print("get detail html start!\n")
            time.sleep(2)
            print("get detail html end!\n")
        if variables.numbers[1] > 20:  # 爬取数量超过20则退出
            break


if __name__== "__main__":
    start_time = time.time()
    thread_list = []
    thread_detail_url = threading.Thread(target=get_detail_url)
    thread_detail_url.start()
    thread_list.append(thread_detail_url)
    for i in range(10):  # 创建10个线程来并行爬取详情页
        html_thread = threading.Thread(target=get_detail_html)
        thread_list.append(html_thread)
        html_thread.start()
    
    for t in thread_list:
        t.join()
    end_time = time.time()
    print("total time:", end_time - start_time)
#    