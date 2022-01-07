#Time: O(n)
#Space:O(n) worst case
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ptr = len(digits) - 1
        while digits[ptr] == 9:
            digits[ptr] = 0
            ptr -= 1
        if ptr < 0:
            return [1] + digits
        else:
            digits[ptr] += 1
        return digits