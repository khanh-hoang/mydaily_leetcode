#Time: O(n)
#Space:O(1)  == O(4)
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maximum = set()
        for i in nums:
            maximum.add(i)
            if len(maximum) > 3:
                maximum.remove(min(maximum))
        
        if len(maximum) == 3:
            return min(maximum)
        return max(maximum)