# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 20:58:43 2018

@author: Dean
p236
给定无序数组，返回其中最长的连续序列的长度
举例：
arr = [100, 4, 200, 1, 3, 2]
返回 4
"""

def longgestConsecutive(arr): #时间复杂度O(n)
    if not arr:
        return 0
    n = len(arr)
    map_ = dict() #map[key] = (left_value,right_value, len) 保存元素key所在的最长连续序列的最左、最右、长度。
    result = 0
    for i in range(n):
        if arr[i] in map_:
            continue
        key = arr[i]
        map_[key] = (i,i,1)
        cur_left = arr[i]
        cur_right = arr[i]
        cur_len = 1
        if key - 1 in map_:
            cur_left = map_[key-1][0]
            cur_len += map_[key-1][2]
        if key + 1 in map_:
            cur_right = map_[key+1][1]
            cur_len += map_[key+1][2]
        #只需要序列的两侧对应的值
        map_[cur_left] = (cur_left,cur_right,cur_len)
        map_[cur_right] = (cur_left,cur_right,cur_len)
        if cur_len > result:
            result = cur_len
    print(map_)
    return result

if __name__ == "__main__":
    arr = [100, 4, 200, 1, 3, 2, 5, 4, 7, 9, 55, 8, 23, 6]
    print(longgestConsecutive(arr))
            
