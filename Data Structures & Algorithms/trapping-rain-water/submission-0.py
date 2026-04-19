class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        level = 0
        ans = 0
        while True:
            while height[l] < level:
                l += 1
                if l == n - 1:
                    return ans

            while height[r] < level:
                r -= 1
                if r == 1:
                    return ans
            
            if l >= r-1:
                return ans

            for i in range(l+1, r):
                if height[i] < level:
                    ans += 1
            level += 1