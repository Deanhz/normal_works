# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 15:28:02 2018
56 medium

@author: Dean
"""

# Definition for an interval.
class Interval:
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class Solution:
    def merge(self, intervals):# by me
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        n = len(intervals)
        if n == 1:
            return intervals
        intervals.sort(key=lambda g:g.start)
        result = []
        first = intervals.pop(0)
        while(intervals):
            second = intervals.pop(0)
            if second.start >= first.start and second.start <= first.end:
                interval = Interval(first.start,max(first.end,second.end))
                first = interval
            else:
                result.append(first)
                first = second
        if not result or first != result[-1]:
            result.append(first)
        return result

if __name__ == "__main__":
    test = [[2,3],[4,5],[6,7],[8,9],[1,10]]
    intervals = []
    for d in test:
        tmp = Interval(d[0],d[1])
        intervals.append(tmp)
    merge_interval = Solution().merge(intervals)
    for d in merge_interval:
        print(d.start,d.end)