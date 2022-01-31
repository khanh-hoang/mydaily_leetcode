#Time: O(logn)
#Space:O(1)
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber != 0:
            columnNumber, r = divmod(columnNumber-1, 26)
            res += chr(r+65)
        return res[::-1]