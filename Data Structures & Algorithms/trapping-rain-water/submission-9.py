class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        
        pre = [0] * n
        pos = [0] * n
        for i in range(1, n):
            pre[i] = max(pre[i-1], height[i-1])
            pos[n-i-1] = max(pos[n-i], height[n-i])

        print(pre)
        print(pos)
        ans = 0
        for i in range(1, n-1):
            h = min(pre[i], pos[i])
            if h > height[i]:
                ans += h - height[i]
        
        return ans