#Time: O(n)
#Space:O(1)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s) - 1
        for i in range(len(s)//2):
            s[i], s[n-i] = s[n-i], s[i]
        """
        s.reverse()
        """
        """
        def helper(start, end, s):
            if start >= end:
                return 
            s[start], s[end] = s[end], s[start]
            return helper(start+1, end - 1, s)
        return helper(0, len(s) - 1, s)
        """
        