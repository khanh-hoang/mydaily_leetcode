#Time: O(n)
#Space:O(n)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        l1 = list(a)
        l2 = list(b)
        carry = 0 
        
        while l1 or l2 or carry:
            if l1: 
                carry += int(l1.pop())
            if l2: 
                carry += int(l2.pop())
                
            res += str(carry % 2)
            carry = carry // 2
        
        return res[::-1]