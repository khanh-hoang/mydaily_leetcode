#Time :O(n)
#Space:O(n)
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        seen = set()
        for i in counter.values():
            if i in seen:
                return False
            seen.add(i)
        return True 