#Time: O(n) n:total number of character in words or chars
#Space:O(1)
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        for word in words:
            for c in word:
                append = True
                if word.count(c) > chars.count(c):
                    append = False
                    break
            if append:
                res += len(word)
        return res
