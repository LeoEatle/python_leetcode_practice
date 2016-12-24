class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #All these variables represent the profit of the current price
        firstBuy = float('-Inf')
        firstSell = 0
        secondBuy = float('-Inf')
        secondSell = 0

        for price in prices:
            if (firstBuy < -price):
                firstBuy = -price
            if (firstSell < price - firstBuy):
                firstSell = price + firstBuy
            if (secondBuy < firstSell - price):
                secondBuy = firstSell - price
            if (secondSell < price - secondBuy):
                secondSell = price + secondBuy

        return secondSell