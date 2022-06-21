class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.first_pos(nums, target)
        last  = self.first_pos(nums, target + 1) -1 
        if first <= last:
            return [first,last]
        return [-1, -1]
    def first_pos(self, x: List[int], a: int):    
        l, r =0, len(x)-1 
        first_pos = len(x)
        
        while l<=r:
            mid = (l+r)//2
            if a <= x[mid]:
                first_pos= mid
                r = mid - 1
            else:
                l = mid + 1
        return first_pos