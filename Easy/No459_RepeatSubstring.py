#Time: O(n)
#Space:O(n)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s:
            return False
        ss = (s+s)[1:-1] 
        return ss.find(s) != -1
    
    """
    Proof:
    s = n*p 
    s+s = n*p + n*p
    (s+s)[1:-1] break the first and the last p
    2np - 2p = np(2-2/n)
    if n = 1, then can't find p in ss 
    if n>= 2, can find p in ss cause np(2-2/n) >= np if n>=2
    """