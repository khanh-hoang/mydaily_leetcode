#Time: O(n)
#Space:O(1)
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        pre = float("-inf")
        for i in s.split():
            if i.isdecimal():
                if int(i) <= pre:
                    return False
                pre = int(i)
        return True