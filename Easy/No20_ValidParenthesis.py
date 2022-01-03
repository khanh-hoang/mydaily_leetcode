#Time : O(n)
#Space: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        mymap = {")":"(", "]":"[", "}":"{"}
        stack = []
        for i in s:
            if i not in mymap:
                stack.append(i)
            else:
                if stack and mymap[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return stack == []
        