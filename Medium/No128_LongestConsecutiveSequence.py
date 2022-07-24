class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0 
        myset = set(nums)
        
        for num in myset:
            if num-1 not in myset:
                curnum = num
                count = 1
                
                while curnum + 1 in myset:
                    count += 1
                    curnum += 1
                
                res = max(res, count)
        return res 