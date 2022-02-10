#Time: O(n) because the number of letter is fixed
#Space:O(1)
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter = Counter(s)
        for c in t:
            if c not in counter or counter[c] == 0:
                return c
            else:
                counter[c] -= 1