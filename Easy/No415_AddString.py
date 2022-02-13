#Time :O(max(n,m))
#Space:O(max(n,m))
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n = len(num1) - 1
        m = len(num2) - 1
        carry = 0
        res = ""
        while n>=0 or m>=0 or carry:
            if n>=0:
                carry += int(num1[n])
                n-=1
            if m>=0:
                carry += int(num2[m])
                m-=1
            res += str(carry % 10)
            carry = carry // 10
        
        return res[::-1]