class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mymap = {}
        for i in nums:
            if i in mymap:
                return i
            else:
                mymap[i] = 1
        return -1