class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0 
        l, r = 0, len(height)-1 
        while l < r:
            area = min(height[r],height[l])*(r-l)
            result = max(result, area)
            if height[r] > height[l]:
                l+=1
            else:
                r-=1
        return result