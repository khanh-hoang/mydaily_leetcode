#Time: O(n)
#Space:O(1)
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        """
        Time: O(n)
        Space:O(n)
        if len(nums) < 2:
            return nums
        odd = []
        even = []
        for i in nums:
            if i%2:
                odd.append(i)
            else:
                even.append(i)
        return even+odd
        """
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] % 2 > nums[j] % 2:
                nums[i], nums[j] = nums[j], nums[i]
                
            if nums[i] % 2 == 0: i+=1
            if nums[j] % 2 == 1: j-=1
        return nums