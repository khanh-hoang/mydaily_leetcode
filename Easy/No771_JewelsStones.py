#Time: O(j + s)
#Space:O(1) because at most 26 * 2 characters
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = set(jewels)
        count = 0
        for i in stones:
            if i in counter:
                count += 1
        return count