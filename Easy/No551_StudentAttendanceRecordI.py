#Time: O(n)
#Space:O(1)
class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        late = 0
        for i in range(len(s)):
            if s[i] == "A":
                absent += 1
                if absent == 2:
                    return False
            if s[i] == "L":
                late += 1
                if late == 3:
                    return False
            else:
                late = 0
        return absent < 2