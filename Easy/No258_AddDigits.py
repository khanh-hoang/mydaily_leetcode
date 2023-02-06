#Time :O(1)
#Space:O(1)
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9
        """
        Time: O(logn)
        Solution 1:
        if num < 10:
            return num
        return self.addDigits(sum([int(i) for i in str(num)]))
        
        Solution 2:
        res = 0
        while num > 0:
            res += num % 10
            num = num // 10
            if num == 0 and res > 9:
                num = res
                res = 0
        return res
        """
        