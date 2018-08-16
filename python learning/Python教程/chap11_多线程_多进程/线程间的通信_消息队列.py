# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 16:17:12 2018

@author: user
"""
from queue import Queue
import threading
import time
import variables



def get_detail_url(queue):  # 爬取文章列表页
    while(True):
        print("get detail url start!\n")
        time.sleep(4)
        for i in range(20): # 假设一次性抓取20个url
            queue.put("http://www.baidu.com/{id}".format(id=i))  # 未处理的item数自动加一
        variables.numbers[0] += 20
        print("get detail url end!\n")
        if variables.numbers[0] >= 20:  # 爬取数量超过20则退出
            break
    
def get_detail_html(queue):  # 爬取文章详情页
    while(True):
        url = queue.get()
        variables.numbers[1] += 1
        # 爬取详情页
        print("get detail html start!\n")
        time.sleep(2)
        print("get detail html end!\n")
        queue.task_done()  # 未处理的item数减一
        if variables.numbers[1] >= 20:  # 爬取数量超过20则退出
            break


if __name__== "__main__":
    start_time = time.time()
    detail_url_queue = Queue(maxsize=1000)  # 消息队列设置最大1000
    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_queue,))
    thread_detail_url.setDaemon(True)  # 主线程结束后，该线程也会结束
    thread_detail_url.start()
    for i in range(10):  # 创建10个线程来并行爬取详情页
        html_thread = threading.Thread(target=get_detail_html, args=(detail_url_queue,))
        html_thread.setDaemon(True)  # 主线程结束后，该线程也会结束
        html_thread.start()
    time.sleep(10)
    detail_url_queue.join()
    end_time = time.time()
    print("total time:", end_time - start_time)