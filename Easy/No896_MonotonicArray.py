#Time: O(n)
#Space:O(1)
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        up = down = True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                up = False
            if nums[i] < nums[i+1]:
                down = False
        return up or down
        """
        Brute force:
        Time :O(2n) = O(n) 
        Space:O(1)
        i = 0
        while i < len(nums) -1:
            if nums[i] <= nums[i+1]:
                i += 1
            else:
                break
        if i == len(nums) -1:
            return True 
        i = 0
        while i < len(nums) -1:
            if nums[i] >= nums[i+1]:
                i += 1
            else:
                break
        if i == len(nums) -1:
            return True 
        """
        