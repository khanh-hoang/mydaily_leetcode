#Time: O(1)
#Space:O(1)
class Solution:
    def findComplement(self, num: int) -> int:
        todo, bit = num, 1
        while todo:
            num = num ^ bit
            bit = bit << 1
            todo = todo >> 1
        return num
    
        """
        return (1<< num.bit_length()) - 1 - num
        """