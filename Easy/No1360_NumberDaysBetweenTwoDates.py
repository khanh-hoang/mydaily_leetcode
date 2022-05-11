#Time: O(n) 
#Space:O(1)
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def isleap(y):
            return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)
        def daysFrom1971(date):
            y, m ,d = map(int, date.split("-"))
            for i in range(1971, y):
                d += 366 if isleap(i) else 365
            if m > 2 and isleap(y):
                d += 1
            while m-1>0:
                m -= 1
                d+= days[m-1]
            return d 
        return abs(daysFrom1971(date1)-daysFrom1971(date2))