#Time: O(n)
#Space:O(1)
class Solution:
    def countBits(self, n:int) -> List[int]:
        def pop_count(x: int) -> int:
            count = 0
            while x != 0:
                x &= x - 1 
                count += 1
            return count
            
        ans = [0] * (n + 1)
        for x in range(n + 1):
            ans[x] = pop_count(x)
    
        return ans                                
        """
        ans = [0] * (n+1)
        for x in range(1, n+1):
            ans[x] = ans[x&(x-1)] + 1
        return ans 
        """