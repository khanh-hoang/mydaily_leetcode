class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = collections.deque([])
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count +=1
                elif grid[i][j] == 2:
                    q.append((i, j, 0))
        res = 0
        while q:
            i, j, res = q.popleft()
            for r, c in ((i, j+1), (i, j-1), (i-1, j), (i+1, j)):
                if 0<=r<m and 0<=c<n and grid[r][c] == 1:
                    grid[r][c] = 2
                    count -= 1
                    q.append((r, c, res+1))
                    
        return res if count == 0 else -1 
            