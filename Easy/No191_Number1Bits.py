#Time: O(1)
#Space:O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n = n&(n-1)
            count += 1
        return count