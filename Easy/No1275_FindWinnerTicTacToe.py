#Time: O(n) n:len(moves)
#Space:O(m) m:len of the board
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3 
        
        row, col = [0] * n, [0] * n
        diagonal = anti_diagonal = 0
        
        #Player A
        player = 1
        
        for r, c in moves:
            row[r] += player
            col[c] += player
            
            if r == c:
                diagonal += player
            if r+c == n-1:
                anti_diagonal += player
            
            if any(abs(line) == n for line in (row[r], col[c], diagonal, anti_diagonal)):
                return "A" if player == 1 else "B"
            player *= -1
            
        return "Draw" if len(moves) == n*n else "Pending"