#Time: O(2n) -> O(n)
#Space:O(10) -> O(1)
class Solution:
    def countPoints(self, rings: str) -> int:
        res = 0
        mymap = defaultdict(set)
        for i in range(1, len(rings), 2):
            mymap[rings[i]].add(rings[i-1])
            
        for v in mymap.values():
            if len(v) == 3:
                res += 1
        return res