# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
import numpy as np


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum([prices[i + 1] - prices[i] for i in range(len(prices)-1) if prices[i + 1] - prices[i] > 0])


prices = [7, 1, 5, 3, 6, 4]
prices=[1,2,3,4,5]
prices=[7,6,4,3,1]
Solution().maxProfit(prices)
