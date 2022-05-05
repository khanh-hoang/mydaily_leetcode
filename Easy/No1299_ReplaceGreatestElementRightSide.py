#Time: O(n)
#Space:O(1)
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curmax = -1 
        for i in range(len(arr))[::-1]:
            cur = arr[i]
            arr[i] = curmax
            curmax = max(curmax, cur)
        return arr