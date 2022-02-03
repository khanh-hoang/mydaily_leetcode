#Time: O(nlogn)
#Space:O(1)
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        #intervals = sorted(intervals, key = lambda x: x[0])
        intervals.sort()
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True