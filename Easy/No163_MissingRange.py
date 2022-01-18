#Time: O(n)
#Space:O(1)
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        def concatRange(lower, upper):
            if lower == upper:
                return str(lower)
            return str(lower) + "->" +str(upper)
        
        res = []
        pre = lower - 1
        for i in range(len(nums) + 1):
            cur = nums[i] if i < len(nums) else upper + 1
            if cur - pre >= 2 : 
                res.append(concatRange(pre + 1, cur -1 ))
            pre = cur
        return res
            
            