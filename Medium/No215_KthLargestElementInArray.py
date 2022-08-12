class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)
        left = [x for x in nums if x > pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]
        
        Left, Mid = len(left), len(mid)
        
        if k <= Left:
            return self.findKthLargest(left, k)
        elif k > (Left+Mid):
            return self.findKthLargest(right, k - (Left+Mid))
        else:
            return mid[0]