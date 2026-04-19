class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_l = height[l]
        max_r = height[r]
        ans = 0
        while l < r:
            if max_l < max_r:
                l += 1
                diff = max_l - height[l]
                if diff > 0:
                    ans += diff
                else:
                    max_l = height[l]
            else:
                r -= 1
                diff = max_r - height[r]
                if diff > 0:
                    ans += diff
                else:
                    max_r = height[r]
        return ans