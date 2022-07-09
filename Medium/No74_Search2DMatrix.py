class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        while l <= r:
            mid = (l+r) // 2
            if matrix[mid][0] == target or matrix[mid][-1] == target:
                return True
            elif matrix[mid][0] < target < matrix[mid][-1]:
                break
            elif matrix[mid][0] > target:
                r = mid - 1 
            elif matrix[mid][-1] < target:
                l = mid + 1
                
        l, r = 0, len(matrix[0]) -1 
        while l <= r:
            newmid = (l+r) // 2
            if matrix[mid][newmid] == target:
                return True
            elif matrix[mid][newmid] < target:
                l = newmid + 1
            else:
                r = newmid - 1
        
        return False 