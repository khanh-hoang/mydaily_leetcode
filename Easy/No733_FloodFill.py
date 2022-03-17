#Time: O(n)
#Space:O(n)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row, col = len(image), len(image[0])
        
        if image[sr][sc] == newColor:
            return image
        ogColor = image[sr][sc]
        def dfs(i, j):
            if i<0 or i>=row or j<0 or j>= col or image[i][j] != ogColor:
                return 
            image[i][j] = newColor
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        dfs(sr, sc)
        return image