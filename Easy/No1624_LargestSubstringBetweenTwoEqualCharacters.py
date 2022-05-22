class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        mymap = {}
        maxdis = 0
        for i, v in enumerate(s):
            if v not in mymap:
                mymap[v] = i
            else:
                maxdis = max(maxdis, i - mymap[v])
        return maxdis - 1