#Time: O(n)
#Space:O(n)
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counter = Counter(heights)
        idx = 1
        res = 0
        
        for h in heights:
            while counter[idx] == 0:
                idx += 1
            if h != idx:
                res += 1
            counter[idx] -= 1
        return res
        
        
        """
        Time: O(nlogn)
        Space:O(n)
        expect = sorted(heights)
        res = 0
        for i in range(len(heights)):
            if expect[i] != heights[i]:
                res += 1
        return res
        """