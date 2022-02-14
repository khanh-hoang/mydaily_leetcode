#Time: O(1)
#Space:O(1)
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((2*n + 0.25)**0.5 - 0.5)
        
        """
        Time: O(logn)
        Space:O(1)
        l, r = 0, n
        while l <= r:
            mid = (l+r) // 2
            cur = mid * (mid+1) // 2
            if cur == n:
                return mid
            elif cur < n:
                l = mid + 1
            else:
                r = mid - 1
        return r
        """
