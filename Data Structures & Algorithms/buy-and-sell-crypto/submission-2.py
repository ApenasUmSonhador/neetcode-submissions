class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestProfit = 0
        bestBuy = prices[0]

        for currValue in prices:
            bestProfit = max(bestProfit, currValue - bestBuy)
            bestBuy = min(bestBuy, currValue)
        return bestProfit