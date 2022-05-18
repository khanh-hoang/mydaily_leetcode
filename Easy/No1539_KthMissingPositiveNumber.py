#Time: O(nlogn)
#Space:O(1)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr)-1
        while l <= r:
            ptr = (l+r) // 2
            if arr[ptr] - ptr - 1 < k:
                l = ptr + 1
            else:
                r = ptr - 1
        #At the end, right + 1 = left
        #And we need arr[r] + (k - (arr[r] - r - 1)) and it's equal
        #to left + k
        return l + k 