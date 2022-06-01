#Time: O(n^2)
#Space:O(1)
class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for a in range(1, n):
            for b in range(a+1, n):
                c = sqrt(a*a+b*b)
                if c > n: 
                    break
                if c <= n and int(c) == c:
                    ans += 2
        return ans