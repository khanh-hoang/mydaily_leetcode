#Time: O(n)
#Space:O(n)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        res = []
        for k,v in cnt1.items():
            cnt1[k] = min(v, cnt2[k])
        
        for k,v in cnt1.items():
            res += [k] * v
        return res
    
        """
        l1 = nums1 if len(nums1) > len(nums2) else nums2
        l2 = nums2 if len(nums2) < len(nums1) else nums1
        
        counter = Counter(nums1)
        res = []
        for num in nums2:
            if num in counter and counter[num] > 0:
                res.append(num)
                counter[num] -= 1
        return res
        """