#Time: O(n)
#Space:O(1)
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        cnt = 1
        res = 1
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                cnt += 1
            else:
                cnt = 1
            res = max(res, cnt)
        return res