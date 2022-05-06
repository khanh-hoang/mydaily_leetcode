#Time: O(n)
#Space:O(1) if output array doesnt count
class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        for i in range(1, n//2 + 1):
            res.append(i)
            res.append(-i)
        if n%2:
            res.append(0)
        return res