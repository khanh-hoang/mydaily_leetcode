#Time: O(nlogn)
#Space:O(1)
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if not s: 
            return "" 
        sets = set(s)
        for i, c in enumerate(s):
            if c.swapcase() not in sets: 
                s0 = self.longestNiceSubstring(s[:i])
                s1 = self.longestNiceSubstring(s[i+1:])
                return max(s0, s1, key=len)
        return s
            