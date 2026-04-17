class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n-2):
            if nums[i] > 0:
                break
            l = i+1
            r = n-1
            while l < r:
                if -nums[i] > nums[l] + nums[r]:
                    l += 1
            
                elif -nums[i] < nums[l] + nums[r]:
                    r -= 1

                else:
                    if not [nums[i], nums[l], nums[r]] in ans:
                        ans.append([nums[i], nums[l], nums[r]])
                    
                    l += 1
        return ans
