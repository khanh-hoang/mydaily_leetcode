#Time: O(n)
#Space:O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        guessSum = len(nums) * (len(nums)+1) // 2
        realSum = sum(nums)
        return guessSum - realSum
        
        """
        Time: O(n)
        Space:O(1)
        Eg : index 0,1,2,3
             value 0,1,3,4
        Then we xor we get the only different value
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
        """