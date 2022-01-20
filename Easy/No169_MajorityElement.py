#Time: O(n)
#Space:O(1)
#Boyer Moore Voting Algorithms
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = 0 
        candidate = None
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        return candidate
        """
        Time: O(n)
        Space:O(n)
        counter = Counter(nums)
        return max(counter.keys(), key=counter.get)
        """