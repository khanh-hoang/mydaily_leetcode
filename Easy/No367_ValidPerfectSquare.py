#Time: O(logn)
#Space:O(1)
#Newton Method
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num<2:
            return True
        x = num // 2
        while x*x > num:
            x = (x+num//x) // 2
        return x * x == num
        
        
        """
        Time :O(logn)
        Space:O(1)
        if num < 2:
            return True 
        left, right = 2, num//2
        while left <= right:
            mid = (left+right) // 2
            guess = mid * mid 
            if guess == num:
                return True
            elif guess > num:
                right = mid - 1
            else:
                left = mid + 1
        return False
        """