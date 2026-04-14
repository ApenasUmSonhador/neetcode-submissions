class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        n_set = set(nums)
        longest = 0
        length = 0

        for x in n_set:
            if x-1 not in n_set:
                length = 1
                x += 1
                while x in n_set:
                    length += 1
                    x += 1
            longest = max(length, longest)
        return longest