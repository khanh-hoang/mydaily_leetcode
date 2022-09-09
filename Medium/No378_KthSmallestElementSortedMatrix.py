class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left, right, N = matrix[0][0], matrix[-1][-1], len(matrix)
        
        def less_than_k(m):
            count = 0
            for row in range(N):
                x = bisect_right(matrix[row],m)
                count += x
            return count 
        
        while left < right:
            mid = (left + right) // 2 
            if less_than_k(mid) < k:
                left = mid + 1
            else:
                right = mid 
        return left