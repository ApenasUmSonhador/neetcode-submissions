class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        l = prices[0]

        for r in prices:
            ans = max(ans, r - l)
            l = min(l, r)
        return ans