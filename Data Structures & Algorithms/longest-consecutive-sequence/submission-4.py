class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
            
        n_set = set(nums)
        count = {}

        for x in n_set:
            if x-1 not in n_set:
                count[x] = 1
                i = x + 1
                while i in n_set:
                    count[x] += 1
                    i += 1
        
        return max(count.values())