#Time: O(n)
#Space:O(1)
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        res = 0
        for i, v in enumerate(colors):
            if v != colors[0]:
                res = max(res, i)
            if v != colors[-1]:
                res = max(res, len(colors) - i - 1)
        return res
        
        """
        Not clean solutions
        l, r = 0, len(colors)-1
        res = 0
        while l < r:
            if colors[l] != colors[r]:
                res = r - l 
                break
            else:
                r -= 1
        l, r = 0, len(colors)-1
        while l < r:
            if colors[l] != colors[r]:
                res = max(res, r-l)
                break
            else:
                l += 1
        return res
        """
        