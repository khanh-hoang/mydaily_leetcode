#Time: O(n)
#Space:O(1)
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign = 1 
        for i in nums:
            if i == 0:
                return 0
            elif i<0:
                sign *= -1
        return sign
        
        """
        Bad solution 
        count = 0
        for i in nums:
            if i < 0:
                count += 1
            elif i == 0:
                return 0
        return -1 if count % 2 else 1
        """
                