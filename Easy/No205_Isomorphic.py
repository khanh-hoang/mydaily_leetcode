#Time: O(n)
#Space:O(1) because the size of ASCII is fixed
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST = {}
        mapTS = {}
        
        for i1, i2 in zip(s,t):
            if (i1 not in mapST) and (i2 not in mapTS):
                mapST[i1] = i2
                mapTS[i2] = i1
            elif mapST.get(i1) != i2 or mapTS.get(i2) != i1:
                return False
        return True 