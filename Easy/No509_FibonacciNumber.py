#Time: O(n)
#Space:O(1)
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        pre = 0 
        cur = 1
        while n > 1:
            nex = pre + cur
            pre = cur
            cur = nex
            n -= 1
        return cur
        """
        Power of math
        Time: O(logn) Space:O(1)
        golden_ratio = (1 + (5 ** 0.5)) / 2
        return int(round((golden_ratio ** N) / (5 ** 0.5)))
        """
        
        
        """
        Dynamic programming solutions
        Time: O(n)
        Space:O(n)
        if n == 0 or n == 1:
            return n
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        """
        
        
        """
        Time: O(2^n)
        Space:O(n)
        Recursion solutions (bad)
        if n < 2: 
            return n
        return self.fib(n-1) + self.fib(n-2)
        """
        