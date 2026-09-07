class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = 100
        max_value = 0
        for i, x in enumerate(prices):
            #x is buying price
            min_value = min(x, min_value)
            #x is selling price
            #x - min value is profit
            #max value is max profit
            max_value = max(max_value, x-min_value)

        return max_value