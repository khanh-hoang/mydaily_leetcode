#Time: O(logn)
#Space:O(1)
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while n%3 == 0:
            n /= 3
        return n == 1
    
        """
        Time: O(1)
        Space:O(1)
        return n > 0 and 3**19 % n == 0
        """