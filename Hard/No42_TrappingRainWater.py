class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0 
        result = 0 
        left, right = 0, len(height) - 1
        leftMax = height[left]
        rightMax = height[right]
        
        while left < right:
            if height[left] < height[right]:
                left += 1 
                leftMax = max (leftMax, height[left])
                result += leftMax - height[left]
            else:
                right -= 1 
                rightMax = max (rightMax, height[right])
                result += rightMax - height[right]
                
        return result
            