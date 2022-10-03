#Time: O(logn)
#Space:O(logn)
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        #Index start from 0 then we have k-1
        return bin(k-1).count('1') & 1
    
    """
    Time: O(n)
    Space:O(n)
    if n == 1:
            return 0
        elif k%2 == 0:
            return 1 if (self.kthGrammar(n-1, k/2) == 0) else 0
        else:
            return 0 if (self.kthGrammar(n-1, (k+1)/2) == 0) else 1
    """