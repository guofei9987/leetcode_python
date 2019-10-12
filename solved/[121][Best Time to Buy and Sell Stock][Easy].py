# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:return 0
        min_price = prices[0]
        min_prices = []
        for i in prices:
            min_price = min(min_price, i)
            min_prices.append(min_price)
        return max([prices[i] - min_prices[i] for i in range(len(prices))])



prices=[7,1,5,3,6,4]
prices=[7,6,4,3,1]
prices=[1]
Solution().maxProfit(prices)


