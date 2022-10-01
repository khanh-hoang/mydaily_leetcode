#Time: O(n)
#Space:O(1)
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}
        ptr = 0
        j = 0 
        res = []
        for i, c in enumerate(s):
            j = max(j, last[c])
            if i == j:
                res.append(i - ptr + 1)
                ptr = i+1
        return res