#Time :O(n)
#Space:O(n)
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(k * (k - 1) // 2 for k in Counter(nums).values())