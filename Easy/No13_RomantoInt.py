#Time: O(n)
#Space: O(1)
class Solution:
    def romanToInt(self, s: str) -> int:
        mymap = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        res = mymap[s[-1]]
        for i in range(len(s)-2, -1, -1):
            if mymap[s[i]] >= mymap[s[i+1]]:
                res += mymap[s[i]]
            else:
                res -= mymap[s[i]]
        return res
        