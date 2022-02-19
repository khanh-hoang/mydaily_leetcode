#Time :O(n)
#Space:O(1)
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()[::-1]
        res = ""
        for i in range(0, len(s), k):
            res += s[i:i+k]
            res += "-"
        return res[:-1][::-1]
        
        """
        s = s.replace("-", "").upper()
        res = ""
        count = 0
        for i in reversed(range(len(s))):
            if count == k:
                res += "-"
                count = 0
            res += s[i]
            count += 1
        return res[::-1]
        """
                