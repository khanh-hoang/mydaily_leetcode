#Time: O(n)
#Space:O(n)
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        ss = s+s
        return ss.find(goal) != -1        