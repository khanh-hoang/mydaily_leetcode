class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        
        def move(i, j):
            for dx, dy in ((0,1), (0,-1), (1,0), (-1,0)):
                if 0<= i+dx <N and 0<= j+dy <N:
                    yield i+dx, j+dy
            
        def dfs(i, j, index):
            res = 0
            grid[i][j] = index
            for x, y in move(i, j):
                if grid[x][y] == 1:
                    res += dfs(x, y, index)
            return res + 1
        
        index = 2
        area = {0:0}
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    area[index] = dfs(i, j, index)
                    index += 1
        
        res = max(area.values())
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 0:
                    possible = set(grid[x][y] for x, y in move(i,j))
                    res = max(res, sum(area[index] for index in possible) + 1)
                    
        return res 
                    
                    
            