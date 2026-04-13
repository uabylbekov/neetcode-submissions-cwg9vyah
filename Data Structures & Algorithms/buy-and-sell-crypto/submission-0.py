class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        minPrice = prices[0]

        for price in prices:
            result = max(result, price-minPrice)
            minPrice = min(minPrice, price)

        return result
