#Time: O(n)
#Space:O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        first = 1
        second = 2
        
        for i in range(2, n):
            third = first + second
            first = second
            second = third
        
        return second

        """
        Time: O(n)
        Space:O(n)
        dp = [0,1,2] + [0] * (n-2)
        for i in range(3,n+1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[n]
        """


        """
        #fibonacci formula:
        #Time: O(logn)
        #Space:O(1)
        return int((((1+sqrt(5))/2) **(n+1)-((1-sqrt(5))/2) ** (n+1))/sqrt(5))
        """
        