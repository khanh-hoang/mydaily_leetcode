class Solution:
    def myAtoi(self, s: str) -> int:
        minInt, maxInt = -2**31, 2**31 - 1 
        i, sign = 0, 1
        s = s.strip()
        
        if len(s) == 0: return 0
        
        if s[0] not in "+-1234567890":
            return 0
        
        if s[0] == "+":
            i +=1 
        elif s[0] == "-":
            sign *= -1
            i +=1
            
        res = 0 
        while i<len(s) and s[i].isdigit():
            if res > maxInt // 10 or (res == maxInt // 10 and int(s[i]) > 7):
                return maxInt if sign == 1 else minInt
            res = res * 10 + int(s[i])
            i+=1
        
        return res*sign