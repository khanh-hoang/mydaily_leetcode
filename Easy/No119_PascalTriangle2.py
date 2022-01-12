#Time: O(n^2) n:rowIndex
#Space:O(n^2)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        output = [[1]]
        for row in range(2, rowIndex+2):
            temp_row = [1]
            for i in range(1, row-1):
                temp_row.append(output[-1][i] + output[-1][i-1])
            temp_row.append(1)
            output.append(temp_row)
        return output[-1]