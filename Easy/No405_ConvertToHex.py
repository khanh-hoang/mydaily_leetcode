#Time: O(logn)
#Space:O(1)
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: return '0'
        if num < 0: 
            num += 2**32
        convert = "0123456789abcdef"
        res = ""
        while num:
            res = convert[(num&15)] + res
            num = num >> 4
        return res