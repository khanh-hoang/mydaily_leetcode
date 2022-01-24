#Time: O(n)
#Space:O(n)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mydict = {}
        
        for i, num in enumerate(nums):
            if num not in mydict:
                mydict[num] = i 
            else:
                if i - mydict[num] <= k:
                    return True
                mydict[num] = i 
        return False 