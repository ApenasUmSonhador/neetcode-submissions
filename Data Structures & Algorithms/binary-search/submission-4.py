class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (r + l)//2
            if nums[m] == target:
                return m # Encontrado!
              
            if nums[m] < target:
                l = m + 1 # Descarta parte esquerda
                
            else:
                r = m - 1 # Descarta parte direita
                
        # Ele não está no array
        return -1