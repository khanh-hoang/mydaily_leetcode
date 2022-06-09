# Time: O(n)
# Space:O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mymap = {}
        
        l = r = 0
        res = 0
        #pakww
        
        while r < len(s):
                
            if s[r] in mymap:
                l = max(mymap[s[r]], l)
                
            res = max(res, r-l+1)
            mymap[s[r]] = r+1
            r+=1
        return res