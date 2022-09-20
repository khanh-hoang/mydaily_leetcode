class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:       
        
        count = Counter()
        count[0] = 1
        mysum, res = 0, 0
        
        for i in nums:
            mysum += i
            res += count[mysum-k]
            count[mysum] += 1
        
        return res 
        