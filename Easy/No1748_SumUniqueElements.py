#Time: O(n)
#Space:O(n)
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        res = 0
        counter = Counter(nums)
        for k in counter.keys():
            if counter[k] == 1:
                res += k
        return res