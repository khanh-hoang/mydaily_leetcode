class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        M = len(s1) 
        N = len(s2)
        res = []
        counterSub = Counter(s1)
        counterStr = Counter(s2[:M-1])
        
        for i in range(M-1, N):
            myidx = i - (M-1)
            counterStr[s2[i]] += 1
            if counterSub == counterStr:
                return True 
            else:
                counterStr[s2[myidx]] -= 1
            if counterStr[s2[myidx]] == 0:
                counterStr.pop(s2[myidx])
            
        return False 