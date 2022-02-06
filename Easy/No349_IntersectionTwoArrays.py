#Time: O(n+m)
#Space:O(n+m)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            if i in nums2:
                res.append(i)
        return set(res)
    
        """
        if both arrays are sorted and the requirement is time: O(n) and space: O(1).           ignore the result's space. 
        case include: duplicate, negative value, single value list, O's, empty.
        Solutions: 
        nums1.sorted() #assume
        nums2.sorted() #assume
        result = []
        
        while nums1 and nums2:
            if nums1[-1] < nums2[-1]:
                nums2.pop()
            elif nums1[-1] > nums2[-1]:
                nums1.pop()
            else:
                if not result or (result and result[-1] != nums1[-1]):
                    result.append(nums1[-1])
                nums1.pop()
                nums2.pop()
        return result
        """
                
        