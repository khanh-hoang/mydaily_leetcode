class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check row 
        for row in board:
            temp = [i for i in row if i != '.']
            if len(temp) != len(set(temp)):
                return False
        
        #check column:
        for row in range(9):
            temp = []
            temp = [board[col][row] for col in range(9) if board[col][row] != '.']
            if len(temp) != len(set(temp)):
                return False
        
        #check box:
        for row in range(0,9,3):
            temp = []
            for col in range(0,9,3):
                square = [board[x][y] for x in range(row,row+3) for y in range(col, col+3)]
                temp = [i for i in square if i!= "."]
                if len(temp) != len(set(temp)):
                    return False
        return True 