#Time: O(n)
#Space:O(1)
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        one_sequence = 0
        for i in range(len(bits)-2, -1, -1):
            if bits[i] == 1:
                one_sequence += 1  
            else: 
                break
        return one_sequence % 2 == 0
                
            
                