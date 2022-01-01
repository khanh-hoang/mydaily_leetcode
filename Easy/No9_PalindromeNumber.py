#Time: O(log10(n)) because we divided the input by 10
#Space: O(1)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x<0 or (x%10 ==0 and x!=0)):
            return False
        revertedNum = 0
        while (revertedNum < x):
            revertedNum = revertedNum*10 + x%10
            x= x // 10
        
        return x == revertedNum or x == revertedNum // 10