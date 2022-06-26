class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ourset =[]
        answer = []
        self.permutation(nums, ourset, answer)
        return answer
    
    def permutation(self, nums, ourset, answer):
        if len(nums) == 0 :
            answer.append(ourset[:])
        for i in range(len(nums)):
            newnums = nums.copy()
            newnums.remove(nums[i])
            ourset.append(nums[i])
            self.permutation(newnums, ourset, answer)
            ourset.pop()