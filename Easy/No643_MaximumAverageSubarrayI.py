#Time: O(n)
#Space:O(1)
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curSum = 0
        for i in range(k):
            curSum += nums[i]
        res = curSum
        for i in range(k, len(nums)):
            curSum += nums[i] - nums[i-k]
            res = max(res, curSum)
        return res / k
