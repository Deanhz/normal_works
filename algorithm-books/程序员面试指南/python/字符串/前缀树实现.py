# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 16:04:47 2018

@author: Dean
p299
"""


class TrieNode:
    def __init__(self):
        self.path = 0  # 有多少个单词共用该节点
        self.end = 0  # 有多少个单词以该节点结尾
        self.map = [None for i in range(26)]  # 直接定址表，查找下一个节点


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def Insert(self, word):  # 插入单词
        if not word:
            return
        n = len(word)
        curNode = self.root
        for i in range(n):
            index = ord(word[i]) - ord("a")
            next_node = curNode.map[index]
            if not next_node:
                curNode.map[index] = TrieNode()
            curNode = curNode.map[index]
            curNode.path += 1
        curNode.end += 1

    def search(self, word):  # 查询单词，返回单词出现的次数
        if not word:
            return 
        n = len(word)
        curNode = self.root
        for i in range(n):
            index = ord(word[i]) - ord("a")
            next_node = curNode.map[index]
            if not next_node:
                return 0
            curNode = curNode.map[index]
        return curNode.end
    
    def delete(self, word):  # 删除某个单词，本方法假设要删除的单词一定存在
        if not word:
            return
        n = len(word)
        curNode = self.root
        for i in range(n):
            index = ord(word[i]) - ord("a")
            next_node = curNode.map[index]
            next_node.path -= 1
            if next_node.path == 0:
                curNode.map[index] = None
                return
            curNode = curNode.map[index]
        curNode.end -= -1  
        return
        
    def prefixNumber(self, pre):  # 返回字符串pre为前缀的单词数量
        if not pre:
            return 0
        n = len(pre)
        curNode = self.root
        for i in range(n):
            index = ord(pre[i]) - ord("a")
            next_Node = curNode.map[index]
            if not next_Node:
                return 0
            curNode = curNode.map[index]
        return curNode.path


if __name__ == "__main__":
    words = ["abc", "bcd", "abc", "abcde", "abctf", "hig"]
    tree = Trie()
    for word in words:
        tree.Insert(word)
    print(tree.search("abc"))
    print(tree.prefixNumber("abc"))
    tree.delete("hig")
    print(tree.search("hig"))






        
        
        
            
            
            
