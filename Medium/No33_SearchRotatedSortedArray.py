class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r) // 2
            if target == nums[mid]:
                return mid 
            
            #left part:
            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else: #target < nums[mid]
                    r = mid - 1
            else: #nums[mid] < nums[l]
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else: #target > nums[mid]
                    l = mid + 1 
        return -1 