#Time: O(n)
#Space:O(1)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        leftsum = 0
        for i, v in enumerate(nums):
            if leftsum == (S-leftsum-v):
                return i
            leftsum += v
        return -1