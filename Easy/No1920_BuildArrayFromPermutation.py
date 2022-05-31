#Time: O(n)
#Space:O(1)
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        #The idea is stored 2 numbers in 1 location 
        #Eg: We store c = a + b*n then we get a by c%n and get b by c//n
        n = len(nums)
        for i in range(n):
            nums[i] = nums[i] + n*(nums[nums[i]]%n)  #%n here to make b<n
        for i in range(n):
            nums[i] = nums[i] // n
        return nums
        
        
        """
        Time :O(n)
        Space:O(n)
        res = [0] * len(nums)
        for i in nums:
            res[i] = nums[nums[i]]
        return res 
        
        """
        