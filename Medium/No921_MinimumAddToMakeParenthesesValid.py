class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        balance = 0
        for i in s:
            balance += 1 if i == "(" else -1
            if balance == -1:
                res += 1
                balance += 1
                
        return res + balance