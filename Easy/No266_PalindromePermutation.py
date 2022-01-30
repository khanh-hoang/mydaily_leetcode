#Time: O(n)
#Space:O(1)
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = set()
        for i in s:
            if i not in count:
                count.add(i)
            else:
                count.remove(i)
        return len(count) <= 1