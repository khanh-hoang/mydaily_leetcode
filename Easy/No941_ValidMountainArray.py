#Time: O(n)
#Space:O(1)
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        ptr = 0 
        n = len(arr)
        while ptr < n-1 and arr[ptr] < arr[ptr+1]:
            ptr += 1
        
        if ptr == 0 or ptr == n - 1:
            return False
        
        while ptr < n-1 and arr[ptr] > arr[ptr+1]:
            ptr += 1
        
        return ptr == n - 1