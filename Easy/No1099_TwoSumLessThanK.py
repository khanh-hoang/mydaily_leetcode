#Time: O(nlogn)
#Space:O(n)
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        res = -1
        while left < right:
            if nums[left] + nums[right] < k:
                res = max(res, nums[left] + nums[right])
                left += 1
            else:
                right -= 1
        return res