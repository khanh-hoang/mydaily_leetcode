#Time: O(n)
#Space:O(n)
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        if counter[0] > 1:
            return True
        for i in arr:
            if counter[i*2] and i != 0:
                return True
        return False