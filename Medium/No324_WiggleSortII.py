class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = (len(nums)+1)//2
        bighalf = nums[n:]
        smallhalf = nums[:n]
        print(bighalf)
        print(smallhalf)
        x,y = 0,0
        for i in range(len(nums)-1,-1,-1):
            if i%2 == 0:
                nums[i] = smallhalf[x]
                x+=1
            else:
                nums[i] = bighalf[y]
                y+=1
                
        