#Time: O(n)
#Space:O(1)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0 
        r = 0
        count = 0
        res = 0
        while r < len(nums):
            if nums[r] == 0:
                count  += 1
            while count == 2:
                if nums[l] == 0:
                    count -= 1
                l += 1
            res = max(res, r-l+1)
            r += 1
        return res