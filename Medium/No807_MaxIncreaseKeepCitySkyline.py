#Time: O(n^2)
#Space:O(n)
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        maxCol = []
        oldSum = 0
        for i in range(col):
            tempMax = 0
            for j in range(row):
                oldSum += grid[j][i]
                if tempMax <= grid[j][i]:
                    tempMax = grid[j][i]
            maxCol.append(tempMax)
        newSum = 0
        for i in range(row):
            for j in range(col):
                grid[i][j] = min(maxCol[j], max(grid[i]))
                newSum += grid[i][j]
        
        return newSum - oldSum