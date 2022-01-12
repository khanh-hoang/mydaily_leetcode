#Time: O(n^2) n:numRows
#Space:O(n^2) 
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        
        for row in range(2, numRows +1):
            temp = []
            temp.append(1)
            for i in range(1, row-1):
                temp.append(res[-1][i-1] + res[-1][i])
            temp.append(1)
            res.append(temp)
            
        return res 