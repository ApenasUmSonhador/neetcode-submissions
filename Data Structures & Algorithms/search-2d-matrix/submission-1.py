class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        line = -1
        line_l = 0
        line_r = len(matrix) - 1
        l = 0
        r = len(matrix[0]) - 1
        
        while line_l <= line_r:
            mid = (line_l + line_r)//2
            if matrix[mid][l]<= target <= matrix[mid][r]:
                line = mid
                break
            if matrix[mid][0] > target:
                line_r = mid-1
            else:
                line_l = mid+1
            

        if line == -1:
            return False
        
        while l <= r:
            mid = (l+r)//2
            if matrix[line][mid] == target:
                return True
            if matrix[line][mid] > target:
                r = mid-1
            else:
                l = mid+1

        return False