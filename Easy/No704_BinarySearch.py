#Time: O(logn)
#Space:O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high =0, len(nums) -1 
        
        while low <= high:
            mid = (low+high) // 2
            if nums[mid] == target:
                return mid 
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1 