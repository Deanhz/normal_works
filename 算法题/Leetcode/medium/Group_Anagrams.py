# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 13:47:15 2018

@author: Dean
"""

class Solution:
    def groupAnagrams(self, strs):#使用map,排序后的单词作为key
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return [[]]
        def word2key(s):
            tmp = list(s)
            tmp.sort()
            return "".join(tmp)
        map_ = dict()
        for word in strs:
            key = word2key(word)
            map_[key] = map_.get(key,[])
            map_[key].append(word)
        return list(map_.values())
    def groupAnagrams2(self, strs): #对单词每个字母出现的次数统计，统计结果转换为唯一的字符串作为key。该方法效率比较低。
        if not strs:
            return [[]]
        
        def word2key(word):
            word2 = word.lower()
            cnt = [0 for i in range(26)]
            for c in word2:
                cnt[ord(c) - ord("a")] += 1
            
            return "".join(list(map(str,cnt)))
        map_ = dict()
        for word in strs:
            key = word2key(word)
            map_[key] = map_.get(key,[])
            map_[key].append(word)
        return list(map_.values())
if __name__ == "__main__":
    test = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams2(test))