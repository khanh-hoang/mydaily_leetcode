#Time: O(nlogn)
#Space:O(1)
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        fix = sorted(boxTypes, key=lambda x: -x[1])
        res = 0
        for i in fix:
            if i[0] <= truckSize:
                res += i[0]*i[1]
            else:
                res += (truckSize) * i[1]
            truckSize -= i[0]
            if truckSize <= 0:
                break
        return res