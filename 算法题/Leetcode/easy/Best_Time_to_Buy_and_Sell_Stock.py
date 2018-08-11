# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 19:32:12 2018

@author: Dean
121 easy Array 
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
总结：自己的解法不够好
"""

class Solution:
    def maxProfit(self, prices): #by me
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        max_profit = 0
        max_price = 0
        length = len(prices)
        for i in range(length-1)[::-1]:#从后往前
            cur = prices[i]
            max_p = max(prices[i+1],max_price)
            max_price = max_p
            if max_p > cur:
                profit = max_p - cur
                max_profit = profit if profit > max_profit else max_profit
        return max_profit
    
    def maxProfit2(self, prices):
        if not prices:
            return 0
        min_price = float("inf")
        result = 0
        for price in prices:
            min_price = min(min_price,price)
            result = max(result,price - min_price)
        return result
        
        
if __name__ == "__main__":
    print(Solution().maxProfit2([7,6,4,3,1]))
                


