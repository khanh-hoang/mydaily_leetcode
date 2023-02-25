#Time: O(m*n)
#Space:O(m*n)
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        res = [[None]*c for i in range(r)]
        if len(mat) == 0 or r*c != len(mat) * len(mat[0]):
            return mat
        row, col = 0, 0 
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                res[row][col] = mat[i][j]
                col += 1
                if col == c:
                    row += 1
                    col = 0
        return res