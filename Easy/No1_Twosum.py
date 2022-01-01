#Time: O(n)
#Space: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mymap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in mymap:
                return [mymap[diff], i]
            else:
                mymap[n] = i 
         