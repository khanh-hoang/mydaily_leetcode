#Time: O(logn)
#Space:O(1)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return self.myPow(1/x, -n)
        
        ans = 1
        cur = x 
        i = n
        while i > 0:
            if i % 2 == 1:
                ans = ans * cur
            cur *= cur
            i = i // 2
            print(cur)
            print(ans)
        return ans
        
        """
        Time: O(logn)
        Space:O(logn)
        if n == 0: return 1
        if n < 0: return self.myPow(1/x, -n)
        lower = self.myPow(x, n//2)
        if n % 2 == 0: return lower*lower
        if n % 2 == 1: return lower*lower*x
        """