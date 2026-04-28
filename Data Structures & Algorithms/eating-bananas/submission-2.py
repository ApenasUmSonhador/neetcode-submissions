class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        while left <= right:
            mid = (left + right)//2
            time = 0
            for pile in piles:
                time += (pile + mid - 1) // mid
            if time > h:
                left = mid + 1
            else:
                right = mid - 1
        return left