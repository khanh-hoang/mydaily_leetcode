#Time: O(n)
#Space:O(1)
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        j = 1
        i = 0
        while i < len(nums):
            if nums[i] % 2:
                while nums[j] % 2:
                    j += 2
                nums[i], nums[j] = nums[j], nums[i]
            i+=2
        return nums
        
        """
        Time: O(n)
        Space:O(n)
        res = [0] * len(nums)
        odd = 1
        even = 0
        for i in nums:
            if i%2:
                res[odd] = i
                odd += 2
            else:
                res[even] = i
                even += 2
        return res
        """
        