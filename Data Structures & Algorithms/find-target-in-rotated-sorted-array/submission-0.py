class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        start = 0
        while l<=r:
            if nums[l]<=nums[r]:
                start = l
                break
            m = (l+r)//2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m+1
        l = 0
        r = len(nums) - 1
        if nums[start] <= target <= nums[r]:
            l = start
        else:
            r = start -1
        
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m+1
            else:
                r = m-1
        return -1