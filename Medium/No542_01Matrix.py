class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = []
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = float('inf')
        
        for i, j in queue:
            for r, c in ((i, j-1), (i, j+1), (i-1, j), (i+1, j)):
                distance = mat[i][j] + 1
                if 0<=r<m and 0<=c<n and mat[r][c] > distance:
                    mat[r][c] = distance
                    queue.append((r,c))
        return mat