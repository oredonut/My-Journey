class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lowest_price = prices [0]
        best_profit = 0

        for current_price in prices:
            if current_price < lowest_price:
                lowest_price = current_price

            profit = current_price -lowest_price

            if profit > best_profit:
                best_profit = profit

        return best_profit
        