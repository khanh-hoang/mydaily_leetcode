#Time: O(n)
#Space:O(1)
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        for i in reversed(range(len(num))):
            k, num[i] = divmod(num[i] + k, 10)
        
        return [int(i) for i in str(k)] + num if k else num
        
        """
        Time: O(n)
        Space:O(n)
        a = int("".join(str(i) for i in num))
        return [int(i) for i in str(a+k)]
        """