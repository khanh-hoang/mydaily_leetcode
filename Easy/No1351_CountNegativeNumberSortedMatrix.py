#Time: O(row + col)
#Space:O(1)
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        count = 0
        i, j = row - 1, 0 #start from bottom left corner
        while i >= 0 and j < col:
            if grid[i][j] < 0:
                count += col - j
                i -= 1
            else:
                j += 1
        return count
        """
        Binary search solution: 
        Time: O(row*log(col))
        Space:O(1)
        def binarySearch(row):
            start, end = 0, len(row) - 1
            while start <= end:
                mid = (start+end) // 2
                if row[mid] < 0:
                    end = mid - 1 
                else:
                    start = mid + 1
            return len(row) - start 
        count = 0
        for row in grid:
            count += binarySearch(row)
        return count
        """
        