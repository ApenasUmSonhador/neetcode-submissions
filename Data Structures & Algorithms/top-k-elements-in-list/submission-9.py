class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for x in range(len(nums) + 1)]
        count = {}

        for x in nums:
            count[x] = count.get(x, 0) + 1

        for n, c in count.items():
            freq[c].append(n)

        ans = []
        
        for i in range(len(freq) - 1, 0, -1):
            for x in freq[i]:
                ans.append(x)
            if len(ans) == k:
                return ans
        