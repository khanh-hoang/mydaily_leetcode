#Time: O(n)
#Space:O(1)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        res = []
        while i <= j:
            if nums[i]**2 > nums[j]**2:
                res.append(nums[i]**2)
                i+=1
            else:
                res.append(nums[j]**2)
                j-=1
        return res[::-1]