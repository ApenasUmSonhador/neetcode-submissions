class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        nums.sort()
        longest = 0
        atual = 1
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                continue
            if nums[i-1] + 1 == nums[i]:
                atual += 1
            else:
                longest = max(longest, atual)
                atual = 1
        return max(longest, atual)