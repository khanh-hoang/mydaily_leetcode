#Time: O(logn)
#Space:O(1)
#Enhance version 1 to better version
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        if reader.get(0) == target:
            return 0
        low, high = 0, 1
        while reader.get(high) < target:
            low = high
            high = high << 1
        
        if reader.get(high) == float("inf"):
            return -1
        
        while low <= high:
            mid = (high+low) >> 1
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1
        
        """
        First solution
        Time :O(logn)
        Space:O(1)
        if reader.get(0) == target:
            return 0
        i = 1
        while reader.get(i) != float("inf") and reader.get(i) < target:
            i*=2
        
        low = 0
        high = i
        while low <= high:
            mid = (high+low) // 2
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1
        """