class Solution:
    def sortSentence(self, s: str) -> str:
        s = s[::-1].split()
        s.sort()
        ans = ""
        for i in s:
            ans += i[1:][::-1] + " "
        return ans[:-1]