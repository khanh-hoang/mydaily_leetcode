class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        index_remove = set()
        stack = []
        for i, c in enumerate(s):
            if c not in "()":
                continue
            elif c == "(":
                stack.append(i)
            elif not stack:
                index_remove.add(i)
            else:
                stack.pop()
        res = []
        index_remove = index_remove.union(set(stack))
        for i, c in enumerate(s):
            if i not in index_remove:
                res.append(c)
        return "".join(res)