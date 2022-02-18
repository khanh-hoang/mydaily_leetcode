#Monotonous stack
#Time: O(n)
#Space:O(n)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hashmap = {}
        
        for i in nums2:
            while stack and i > stack[-1]:
                hashmap[stack.pop()] = i
            stack.append(i)
            
        while stack:
            hashmap[stack.pop()] = -1
            
        res = [0]*len(nums1)
        for i in range(len(nums1)):
            res[i] = hashmap[nums1[i]]
        return res
        
        """
        Brute force solution
        Time: O(n*m)
        Space:O(1)
        res = []
        for i in nums1:
            idx = nums2.index(i)
            while idx < len(nums2)-1:
                if nums2[idx+1] > i:
                    res.append(nums2[idx+1])
                    break
                else:
                    idx+=1
            if idx == len(nums2) - 1:
                res.append(-1)
        return res
        """
        