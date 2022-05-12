#Time: O(n)
#Space:O(n)
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        if paths == []:
            return ""
        mymap = {}
        for i,j in paths:
            mymap[i] = j
        for v in mymap.values():
            if v not in mymap:
                return v