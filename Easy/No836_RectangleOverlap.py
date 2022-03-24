#Time: O(1)
#Space:O(1)
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return  (min(rec1[2], rec2[2]) > max(rec1[0], rec2[0])) and \
                (min(rec1[3], rec2[3]) > max(rec1[1], rec2[1]))
        """
        # check if either rectangle is actually a line
        if (rec1[0] == rec1[2] or rec1[1] == rec1[3] or \
            rec2[0] == rec2[2] or rec2[1] == rec2[3]):
            return False

        return not (rec1[2] <= rec2[0] or  
                    rec1[3] <= rec2[1] or  
                    rec1[0] >= rec2[2] or  
                    rec1[1] >= rec2[3])   
        """