class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r = len(prices) - 1
        ans = 0
        l = r-1
        while l >= 0:
            if prices[l] > prices[r]:
                r = l
            else:
                ans = max(ans, prices[r] - prices[l])
            l -= 1
        return ans