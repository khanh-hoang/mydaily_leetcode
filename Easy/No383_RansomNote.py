#Time: O(n)
#Space:O(n)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine)
        for i in ransomNote:
            counter[i] -= 1
            if counter[i] < 0:
                return False
        return True
    """
    return not Counter(ransomNote) - Counter(magazine)
    """
