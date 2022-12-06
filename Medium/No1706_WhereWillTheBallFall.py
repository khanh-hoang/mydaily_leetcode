#Time: O(row * col)
#Space:O(col)
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        row, col = len(grid), len(grid[0])
        res = []
        for i in range(col):
            curRow = 0 
            curCol = i
            while curRow < row:
                if curCol+1 < col and (grid[curRow][curCol] == grid[curRow][curCol+1] == 1):
                    curRow += 1
                    curCol += 1
                elif curCol-1 > -1 and (grid[curRow][curCol] == grid[curRow][curCol-1] == -1):
                    curRow += 1
                    curCol -= 1
                else:
                    break
            if curRow == row:      
                res.append(curCol)  
            else:
                res.append(-1)
        return res