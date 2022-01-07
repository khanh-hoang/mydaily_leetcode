#Time: O(1)
#Space:O(1)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        res = int(e**(log(x)*0.5))
        return res if (res+1)*(res+1) > x else res + 1