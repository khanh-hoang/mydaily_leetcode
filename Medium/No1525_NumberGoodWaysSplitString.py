#Time: O(n)
#Space:O(n)
class Solution:
    def numSplits(self, s: str) -> int:
        l, r = set(), Counter(s)
        res = 0
        for ch in s:
            l.add(ch)
            r[ch] -= 1
            if r[ch] == 0:
                r.pop(ch)
            if len(l) == len(r):
                res += 1
        return res