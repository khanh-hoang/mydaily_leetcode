#Time: O(n)
#Space:O(1) cause at most 26 character
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        #Important line
        if len(set(pattern)) != len(set(s)):
            return False
        wordmap = {}
        for i in range(len(s)):
            if pattern[i] not in wordmap:
                wordmap[pattern[i]] = s[i]
            elif wordmap[pattern[i]] != s[i]:
                return False
        return True 