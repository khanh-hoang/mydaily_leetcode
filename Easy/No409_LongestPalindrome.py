class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        res = 0
        for k, v in count.items():
            if v%2: 
                res += v - 1 
                count[k] -= v - 1
            else:
                res += v
                count[k] -= v 
        for v in count.values():
            if v != 0:
                return res + 1 
        return res 
        