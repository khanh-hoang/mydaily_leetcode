#Time: O(n)
#Space:O(1)
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0 
        prev, cur = 0, 1
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                ans += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1
        
        return ans + min(prev, cur)
        """
        Time :O(n)
        Space:O(n)
        group = [1]
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                group.append(1)
            else:
                group[-1] += 1
        ans = 0
        for i in range(1, len(group)):
            ans += min(group[i], group[i-1])
        return ans
        """