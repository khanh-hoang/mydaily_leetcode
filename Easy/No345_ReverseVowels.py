#Time: O(n)
#Space:O(1)
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ["a", "i", "o", "e", "u", "A", "I", "O", "E", "U"]
        if len(s) < 2:
            return s
        s = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            while s[l] not in vowel and l<r:
                l+=1
            while s[r] not in vowel and l<r:
                r-=1
            s[r], s[l] = s[l], s[r]
            l+=1
            r-=1
            
        print(s)
        return "".join(s)