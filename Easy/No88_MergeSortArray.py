#Time: O(n+m)
#Space:O(1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr = len(nums1) - 1
        while m>0 and n>0: 
            if nums1[m-1] <= nums2[n-1]:
                nums1[ptr] = nums2[n-1]
                n-=1
            else:
                nums1[ptr] = nums1[m-1]
                m-=1
            ptr-=1
        while m>0:
            nums1[ptr] = nums1[m-1]
            m-=1
            ptr-=1
        while n>0:
            nums1[ptr] = nums2[n-1]
            n-=1
            ptr-=1
            