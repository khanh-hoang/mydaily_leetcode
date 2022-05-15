#Time: O(n)
#Space:O(1)
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        #The idea is stored a pair of number in 1 number
        #Shiftleft 10 place for second number, and then get both of them
        #Shift right, and AND gates to get. max num = 1000 then we shift 10 bits
        i = n - 1
        for j in range(len(nums)-1, n-1,-1):
            nums[j] = nums[j] << 10     #shilf numY to get space for numX
            nums[j] = nums[j] | nums[i] #get pair of Y, X
            i -= 1
            
        i = 0
        for j in range(n, len(nums)):
            numX = nums[j] & 1023       #1023 is 10 bits 11111111111 to get X
            numY = nums[j] >> 10        #shift 10 bits to get Y
            nums[i] = numX
            nums[i+1] = numY
            i+=2
            
        return nums
            
        """
        i = 0
        j = len(nums)//2
        res = [0] * len(nums)
        k = 0 
        while k<len(nums):
            res[k] = nums[i]
            res[k+1] = nums[j]
            i+=1
            j+=1
            k+=2
        return res
        """