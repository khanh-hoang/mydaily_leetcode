#Time: O(n)
#Space:O(n)
#Or we can use hashmap
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (3*sum(set(nums)) - sum(nums))//2