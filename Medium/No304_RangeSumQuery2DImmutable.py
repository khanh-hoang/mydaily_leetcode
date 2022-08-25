class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        for row in range(len(matrix)):
            for col in range(1, len(matrix[0])):
                matrix[row][col] += matrix[row][col-1] 
                
        for row in range(1, len(matrix)):
            for col in range(len(matrix[0])):
                matrix[row][col] += matrix[row-1][col]
                
        self.matrix = matrix
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bigsum = self.matrix[row2][col2]
        topsum = self.matrix[row1-1][col2] if row1 else 0
        leftsum = self.matrix[row2][col1-1] if col1 else 0
        smallsum = self.matrix[row1-1][col1-1] if row1 and col1 else 0
        
        return bigsum - topsum - leftsum + smallsum

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)