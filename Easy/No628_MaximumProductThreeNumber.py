#Time :O(n)
#Space:O(1)
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        min1 = min2 = float("inf")
        max1 = max2 = max3 = float("-inf")
        
        for n in nums:
            if n <= min1:
                min2 = min1
                min1 = n
            elif n <= min2:
                min2 = n
            
            if n >= max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n >= max2:
                max3 = max2
                max2 = n
            elif n >= max3:
                max3 = n
        
        return max(min1*min2*max1, max1*max2*max3)
               
        
        return max(mymin[0]*mymin[1]*mymax[0], mymax[0]*mymax[1]*mymax[2])
        """
        Time: O(nlogn)
        Space:O(logn)
        nums.sort()
        s1 = nums[0] * nums[1] * nums[-1]
        s2 = nums[-1] * nums[-2] * nums[-3]
        return max(s1, s2)
        """
        