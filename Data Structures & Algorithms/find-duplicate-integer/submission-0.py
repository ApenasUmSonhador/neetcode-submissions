class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        saw=set()
        for x in nums:
            if x in saw:
                return x
            saw.add(x)
