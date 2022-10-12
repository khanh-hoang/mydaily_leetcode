#Time: O(n)
#Space:O(1)
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        res = bal = 0
        for i, v in enumerate(s):
            if v == "(":
                bal += 1
            else:
                bal -= 1
                if s[i-1] == "(":
                    res += 1<<bal
        return res
            
        """
        Time: O(n)
        Space:O(n)
        stack = [0]
        for c in s:
            if c == "(":
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += (2*v, 1)
        return stack.pop()
        """