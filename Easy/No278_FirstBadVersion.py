# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):
#Time: O(nlogn)
#Space:O(1)
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n 
        while low < high:
            mid = (low+high) // 2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid+1
        return low