class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        from math import ceil
        r = max(piles)
        l = 1
        prev = r
        while l<=r:
            m = (r+l)//2
            time = 0
            for x in piles:
                time += ceil(x/m)
            if time > h:
                l = m+1
            else:
                r = m-1
                prev = min(prev,m)
        return prev