class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        res = []
        for num in range(len(nums)):
            res.append(product)
            product *= nums[num]
        #1,1,2,6  
        product = 1
        for num in range(len(nums)-1, -1, -1):
            res[num] = res[num] * product
            product  *= nums[num]
        return res
