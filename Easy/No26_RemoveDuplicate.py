#Time: O(n)
#Space:O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        ptr = 0
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                ptr +=1
                nums[ptr] = nums[i+1]
        return ptr+1
        