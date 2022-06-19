class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, idx):
            j = len(nums) - 1
            while idx < j:
                nums[idx], nums[j] = nums[j], nums[idx]
                idx += 1
                j -=1
        
        ptr = len(nums) - 2
        while ptr>=0 and nums[ptr+1] <= nums[ptr]:
            ptr -= 1
            
        if ptr>=0:
            i = len(nums)-1
            while nums[i] <= nums[ptr]:
                i -= 1
            nums[i], nums[ptr] = nums[ptr], nums[i]
            
        reverse(nums, ptr+1)