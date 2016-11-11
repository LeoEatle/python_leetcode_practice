#coding: utf-8

class Solution(object):
    def maxProfit(self, prices):
        """

        :param prices: List[int]:
        :return: int
        """
        if len(prices) == 0:
            return 0
        min_price = prices[0]
        profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            if price - min_price > profit:
                profit = price - min_price
        return profit


s = Solution()
print s.maxProfit([1,2,3,4])