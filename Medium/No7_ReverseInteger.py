class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        temp = abs(x)
        while (temp > 0):
            res = res * 10 + temp % 10
            temp = temp // 10
        
        if (res>2147483647 or res<-2147483648):
            return 0
        if x <0:
            return res*-1
        return res 
            