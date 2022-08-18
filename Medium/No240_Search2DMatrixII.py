#Time: O(m+n)
#Space:O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        
        r, c = row - 1, 0 
        while r > -1 and c < col:
            val = matrix[r][c]
            if val == target:
                return True 
            elif val > target:
                r -= 1
            else:
                c += 1
        return False 