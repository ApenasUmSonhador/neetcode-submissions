class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, x in enumerate(nums):
            if x in d.keys():
                return [d[x], i]
            d[target-x] = i