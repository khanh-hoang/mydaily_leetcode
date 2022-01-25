#Time: O(n)
#Space:O(1)
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        a = 0
        res = []
        for b in range(len(nums)):
            if b + 1 < len(nums) and nums[b] == nums[b+1] - 1:
                continue
            if b != a:
                res.append(str(nums[a])+"->"+str(nums[b]))   
            else:
                res.append(str(nums[a]))
            a = b + 1
        return res
            
        
                