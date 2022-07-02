class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastgood_position = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= lastgood_position:
                lastgood_position = i 
        return lastgood_position == 0