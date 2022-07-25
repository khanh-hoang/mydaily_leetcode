class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(i, j):
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j] != "O":
                return 
            board[i][j] = "!" 
            dfs(i, j+1)
            dfs(i, j-1)
            dfs(i-1, j)
            dfs(i+1, j)
        m = len(board)
        n = len(board[0])
        if m<3 and n<3:
            return 
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "!":
                    board[i][j] = "O"
                    