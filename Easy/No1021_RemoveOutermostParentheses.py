#Time: O(n)
#Space:O(n)
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""
        stack = []
        track = ""
        for i in range(len(s)):
            if s[i]==")" and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(s[i])
            track += s[i]
            if not stack and track:
                res += track[1:-1]
                track = ""
            print(stack)
            print(track)
        return res