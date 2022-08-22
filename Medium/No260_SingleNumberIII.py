#Time: O(n)
#Space:O(1)
#Can do hashmap for O(n) and O(n)
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        bitmask = 0
        for num in nums:
            bitmask ^= num
        # rightmost 1-bit diff between x and y
        diff = bitmask & (-bitmask)
        #diff will take the unique bit that the other doesnt have
        x = 0
        for num in nums:
            # bitmask which will contain only x
            if num & diff:
                x ^= num
        
        return [x, bitmask^x]