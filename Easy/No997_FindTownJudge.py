#Time: O(e) e: number of edges
#Space:O(n)
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n-1:
            return -1
        
        intrust = [0] * (n+1)
        outtrust = [0] * (n+1)
        
        for i, j in trust:
            outtrust[i] += 1
            intrust[j] += 1
        
        for i in range(1, n+1):
            if intrust[i] == n -1 and outtrust[i] == 0:
                return i
        return -1