#Time: O(n)
#Space:O(n)
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}
        
        for i in sorted(arr):
            if i not in rank:
                rank[i] = len(rank) + 1
            
        return map(lambda a: rank[a], arr)