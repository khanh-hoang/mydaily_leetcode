#Time: O(n)
#Space:O(1)
class Solution:
    def maxPower(self, s: str) -> int:
        temp = 1
        res = 1
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                temp = 1
            else:
                temp +=1
            res = max(res, temp)
        return res