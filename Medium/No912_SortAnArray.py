class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr1, arr2):
            ptr1 = ptr2 = 0 
            res = []
            while ptr1<len(arr1) and ptr2<len(arr2):
                if arr1[ptr1] < arr2[ptr2]:
                    res.append(arr1[ptr1])
                    ptr1 += 1
                else:
                    res.append(arr2[ptr2])
                    ptr2 += 1
            
            res.extend(arr1[ptr1:])
            res.extend(arr2[ptr2:])
            return res
        
        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) >> 1
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])
            return merge(left, right)
        
        return mergeSort(nums)