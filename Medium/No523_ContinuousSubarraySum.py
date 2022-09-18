class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        res = {0: -1}
        sum_mod = 0 
        for i, n in enumerate(nums):
            sum_mod = (sum_mod + n) % k
            if sum_mod in res and i - res[sum_mod] > 1:
                return True
            elif sum_mod not in res:
                res[sum_mod] = i
        return False